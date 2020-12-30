
typedef struct s_char_array {
    char * par;
    int length;
} CharArray;

char * pseudo_random_sequence_generation(int c_init, int length);
//char * scrambling(char * b__q, int size_bq, int q, int n_RNTI, int N_ID_cell, int n_s, int x, int y);
//CharArray pseudo_random_sequence_generation(int c_init, int length);
int scrambling(char * b__q, int size_bq, int q, int n_RNTI, int N_ID_cell, int n_s, int x, int y, char * b);
