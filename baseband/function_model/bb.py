#! $PATH/python
# -*- coding: utf-8 -*-

# file name: bb.py
# author: lianghy
# time: 11/24/2020 9:37:49 AM

"""This is LTE baseband function model."""

import collections
import numpy

# 1. PUSCH
#### 1.1 scrambing
#### 1.1 scrambing
def scrambing(b_q, M_bit_q):
    """spread spectrum"""
    i = 0
    # n_RNTI: RNTI associated with the PUSCH transmission as described in clause 8 in 3GPP TS 36.213 [4]
    c_init = n_RNTI * 2**14 + q * 2**13 + n_s//2 * 2**9 + N_ID_cell
    c_q = pseudo_random_sequence_generation(c_init, M_bit_q)
    for i in range(M_bit_q):
        if b_q[i] == x:
            b_w[i] = 1
        else:
            if b_q[i] == y:
                b_w[i] = b_q[i-1]
            else:
                b_w[i] = (b_q[i] + c_q[i]) % 2

########### public fuctions

def pseudo_random_sequence_generation(c_init, length):
    """ get a random `length` bit secquence.
    the generater secquence is a 31 bit Gold sequence.

    Parameters
    ==========

    * c_init: initial value for caculate second m-secquece.
    * length: set the total result secquece length, the length of c[n].

    """
    N_c = 1600
    x_1 = collections.deque()
    x_2 = collections.deque()
    c = collections.deque()
    # math: c_init = \sum_{i=0}^{30} x_2(i) . 2^i
    tv = 2**31
    for x in range(31):
        if c_init >= tv:
            x_2.append(1)
            c_init -= tv
        else:
            x_2.append(0)
        tv >>= 1
    # x_1[n+31] = (x_1[n+3] + x_1[n])%2
    # x_2[n+31] = (x_2[n+3] + x_2[n+2] + x_2[n+1] +x_2[n])%2
    # c[n] = (x_1[n+N_c]+x_2[n+N_c])%2
    for n in range(l600):
        x_1.append((x_1[n+3] + x_1[n])%2)
        x_2.append((x_2[n+3] + x_2[n+2] + x_2[n+1] +x_2[n])%2)
    for n in range(length):
        m = n+1600
        x_1.append((x_1[m+3] + x_1[m])%2)
        x_2.append((x_2[m+3] + x_2[m+2] + x_2[m+1] +x_2[m])%2)
        c.append((x_1[n+N_c]+x_2[n+N_c])%2)
    return c


if __name__ == "__main__":
    print("bb.py")
