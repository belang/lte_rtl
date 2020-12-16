#! $PATH/python
# -*- coding: utf-8 -*-

# file name: bb.py
# author: lianghy
# time: 11/24/2020 9:37:49 AM

"""This is LTE baseband function model."""

# R14

# name specfication:
# most name are the same as them in 3GPP TS R14 doc.
# Name Rules:
# 
# The presentation for variables in 3GPP
# ======================================
# 
# * The first charaters of a variable is the same as in 3GPP.
# * The first underscore after the charaters indicates the subscript, 
#   and the seconde underscore indicates the superscript
# 
# for example, a_sub_up means the variable name is a, the sub means subscript, the up means superscript.
# in a__up, up still means superscript.
# that means, the string after the first _ is subscript, after the second _ is superscript.
#
# Greek alphabet
# ==============
#
# Greek alphabet is start with XL_
#
# Variables Defination
# ====================
#
# The followings are some variable definations:
#
# * b__q: the binarys of q(codeword)
# * b__qw: the binarys of after scrabling

import collections
import math
import numpy
#from . import lte_words as lw

# constant value
C1 = 1/math.sqrt(2)
VQPSK_I = C1
VQPSK_Q = VQPSK_I
W_PUSCH = {
    # P = 2
    '2':[[[numpy.array([[C1],[C1]])], [numpy.array([[C1,0],[0,C1]])]],        # codebook_index = 0
         [[numpy.array([[C1],[-1*C1]])], []],                                 # codebook_index = 1
         [[numpy.array([[C1],[(1j)*C1]])], []],                               # codebook_index = 2
         [[numpy.array([[C1],[(-1j)*C1]])], []],                              # codebook_index = 3
         [[numpy.array([[C1],[0]])], []],                                     # codebook_index = 4
         [[numpy.array([[0],[C1]])], []],                                     # codebook_index = 5
        ],
    # P = 4
    '4':[]
        }

# 1. PUSCH
#### 1.1 scrambing
#### 1.1 scrambing
def scrambing(b__q, q, n_RNTI, N_ID_cell, n_s, x, y):
    """spread spectrum.
    result is a same length bit sequence of the b__q.
    
    Parameters
    ==========

    * b__q: [bit], codeword bits.
    * q: codeword parameter, Up to two codewords can be transmitted in one subframe, i.e., q in [0, 1] . In the case of single-codeword transmission, q in [0].
    * n_RNTI: RNTI associated with the PUSCH transmission as described in clause 8 in 3GPP TS 36.213 [4].
    * n_s: Slot number within a radio frame
    * N_ID_cell: cell ID.
    * x and y are tags defined in 3GPP TS 36.212 [3] clause 5.2.2.6.

    """
    i = 0
    c_init = n_RNTI * 2**14 + q * 2**13 + n_s//2 * 2**9 + N_ID_cell
    M_bit_q = len(b__q)
    c_q = pseudo_random_sequence_generation(c_init, M_bit_q)
    for i in range(M_bit_q):
        if b__q[i] == x: # ACK/NACK or Rank Indication placeholder bits
            b_w[i] = 1
        else:
            if b__q[i] == y: # ACK/NACK or Rank Indication repetition placeholder bits
                b_w[i] = b_w[i-1]
            else:   # Data or channel quality coded bits, Rank Indication coded bits or ACK/NACK coded bits
                b_w[i] = (b__q[i] + c_q[i]) % 2
    return b__qw

def modulation(b__qw, mod_type):
    """one methord in QPSK, 16QAM, 64QAM, 256QAM.
    """
    if mod_type == 'QPSK':
        d__q = QPSK(b__qw)
    elif mod_type == '16QAM':
        d__q = QAM16(b__qw)
    elif mod_type == '64QAM':
        d__q = QAM64(b__qw)
    elif mod_type == '256QAM':
        d__q = QAM256(b__qw)
    else:
        raise TypeError("Not support modulation type in LTE.")
    return d__q

def layer_mapping(d__0, d__1=0, num_layer=1, num_codeword=1):
    """transmit codeword to layers.
    result is x=[x(XL_v-1)...].
    XL_v is the number of layer."""
    x = []
    #x = [collections.deque()] * num_layer
    if num_layer == 1:
        if num_codeword == 1:
            x.append(d__0)
        else:
            raise ValueError(f"not support config: layer={num_layer} and codeword={num_codeword}.")
    elif num_layer == 2:
        if num_codeword == 1:
            x.append(d__0[0::2])
            x.append(d__0[1::2])
        elif num_codeword == 2:
            x.append(d__0)
            x.append(d__1)
        else:
            raise ValueError(f"not support config: layer={num_layer} and codeword={num_codeword}.")
    elif num_layer == 3:
        if num_codeword == 2:
            x.append(d__0)
            x.append(d__1[0::2])
            x.append(d__1[1::2])
        else:
            raise ValueError(f"not support config: layer={num_layer} and codeword={num_codeword}.")
    elif num_layer == 4:
        if num_codeword == 2:
            x.append(d__0[0::2])
            x.append(d__0[1::2])
            x.append(d__1[0::2])
            x.append(d__1[1::2])
        else:
            raise ValueError(f"not support config: layer={num_layer} and codeword={num_codeword}.")
    else:
        raise ValueError(f"not support config: layer={num_layer} and codeword={num_codeword}.")
    return x

def precoding(y, num_layer=1, P=1, codebook_index=0):
    """support P=2, 4.
    result is z=[z(P-1)]

    Parameters
    ==========

    y: two dimension data.

    """
    if P=1:
        z = y
    else:
        try:
            w = W_PUSCH[P][codebook_index][num_layer]
            z = w * y
        except IndexError as e:
            raise NotImplementedError("precoding")
    return z

def RE_mapping(z, map_type=0, RB_start=0, L_CRBs=100, N_RB_UL=100, N_symb_UL=7, N_sc_RB=12):
    """mapping to physical resource.
    Default config is:
        * UPLINK bandwidth: 20MHz
        * Normal cyclic prefix
        * allocate all RB to UE
    Supported mode:
        * normal mode
        * not SRS
    """
    a = collections.deque()
    redundence = [0+0j,0+1j,1+0j,0-1j]*(N_RB_UL//4) # 冗余信息。
    if map_type == 0:
        # 从RB_start开始连续分配
        rb_index = [0]*RB_start + [1]*L_CRBs + [0]*(N_RB_UL-RB_start-L_CRBs)
        pass
    else:
        raise NotImplementedError(f"RE mapping type: {map_type}")
    for zl in z:
        ta = []
        zi = iter(zl)
        ri = iter(redundance)
        for l in range(N_symb_UL):
            for i in len(rb_index):
                if rb_index[i]: # resoure is allocated to UE.
                    try:
                        for k in range(N_sc_RB):
                            ta.append(next(zi))
                    except IndexError as e:
                        break
                else:
                    for k in range(N_sc_RB):
                        ta.append(next(ri))
        a.append(ta)
        # for i in len(rb_index):
            # if rb_index[i]: # resoure is allocated to UE.
                # try:
                    # for l in range(N_symb_UL):
                        # for k in range(N_sc_RB):
                            # a.append(next(zi))
                # except IndexError as e:
                    # break
            # else:
                # for l in range(N_symb_UL):
                    # for k in range(N_sc_RB):
                        # a.append(next(ri))

def generate_SCFDMA(a, N_RB_UL=100, N_sc_RB=12, N_symb_UL=7):
    """generate SC-FDMA Symbol.
    t = [tp0=[array,], tp1]"""
    flen = N_RB_UL * N_sc_RB
    t = []
    for ap in a:
        tp = []
        for l in range(N_symb_UL):
            start_point = flen * l
            ttt = numpy.fft.ifft(numpy.array(ap[start_point:start_point+flen], dtype=numpy.complexfloating), flen)
            tp.append(list(ttt))
            ## TODO: slot divide!!!!
        if N_symb_UL == 7:
            tp[0] = tp[0][-160:] + tp[0]
            for x in range(1,7,1):
                tp[x] = tp[x][-144:] + tp[x]
        else:
            raise NotImplementedError(f'CP type: {N_symb_UL}')
        t.append(tp)
    return t

########### public fuctions

def pseudo_random_sequence_generation(c_init, length):
    """ get a random `length` bit sequence.
    the generater sequence is a 31 bit Gold sequence.

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
    # caculate x_2 by c_init.
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
    for n in range(N_c):
        x_1.append((x_1[n+3] + x_1[n])%2)
        x_2.append((x_2[n+3] + x_2[n+2] + x_2[n+1] +x_2[n])%2)
    for n in range(length):
        m = n+N_c
        x_1.append((x_1[m+3] + x_1[m])%2)
        x_2.append((x_2[m+3] + x_2[m+2] + x_2[m+1] +x_2[m])%2)
        c.append((x_1[m]+x_2[m])%2)
    return c

def QPSK(din, MUSTIdx='00', XL_fai=(0,0)):
    """QPSK"""
    dout = collections.deque()
    for i in range(len(din), 2):
        if MUSTIdx == '00':
            try:
                dout.append(eval(f'{VQPSK_I*(din[i]*(-2)+1)}+j{VQPSK_Q*(din[i+1]*(-2)+1)}'))
            except IndexError as e:
                return dout
            except Exception as e:
                return e
        else:
            raise NotImplementedError("")
    return dout

if __name__ == "__main__":
    print("bb.py")
