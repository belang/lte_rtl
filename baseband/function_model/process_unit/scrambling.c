
#include <math.h>
#include <process.h>

CharArray scrambling(char * b__q, int size_bq, int q, int n_RNTI, int N_ID_cell, int n_s, int x, int y)
{
    CharArray out;
    char b__qw[size_bq];
    char b_w[size_bq];
    int c_init = (int) (n_RNTI * pow(2, 14) + q * pow(2, 13) + n_s/2 * pow(2, 9) + N_ID_cell);
    char * c_q;
    CharArray ta = pseudo_random_sequence_generation(c_init, size_bq);
    for (int i = 0; i < size_bq; i++) {
        if (b__q[i] == x) // ACK/NACK or Rank Indication placeholder bits
            b_w[i] = '1';
        else {
            if (b__q[i] == y) // ACK/NACK or Rank Indication repetition placeholder bits
                b_w[i] = b_w[i-1];
            else  // Data or channel quality coded bits, Rank Indication coded bits or ACK/NACK coded bits
                b_w[i] = (char) (b__q[i] + *c_q+i) % 2;
        }
    }
    out = b__qw;
    return 1;
}
