#include <process.h>
#include <math.h>
#include <stdio.h>

char * pseudo_random_sequence_generation(int c_init, int length)
{
    char * out;
    int N_c = 1600;
    int tdata_size = length+N_c;
    char x_1[tdata_size], x_2[tdata_size+1], c[length];
    int tv = (int)pow(2, 31);
    int i_m;
    for (int i = 0; i < tdata_size; i++) {
        x_2[i] = '0';
        x_1[i] = '0';
    }
    x_2[tdata_size] = '\0';
    for (int i = 0; i < 31; i++) {
        if (c_init >= tv) {
            x_2[i] = '1';
            c_init -= tv;
        }
        //else {
            //x_2[i] = '0';
        //}
        //x_1[i] = '0';
        tv >>= 1;
        //printf("index is %d, x_2 in generator is %s\n", i, x_2);
    }
    printf("run here\n");
    printf("print in char: ");
    for (int i = 0; i < tdata_size; i++) {
        printf("%c", x_2[i]);
    }
    printf("\n");
    printf("print in string: ");
    printf("%s", x_2);
    printf("\n");
    out = x_2;
    //out.par = x_2;
    //out.length = tdata_size;
    //int ti = 0;
    //printf("result in function is: ");
    //for (int i = 0; i < tdata_size; i++) {
        //printf("%c", *out);
        //out++;
    //}
    //printf("\n");
    //for (int i = 0; i < N_c; i++) {
        //x_1[i+31] = (char) ((int)x_1[i+3] + (int)x_1[i])%2;
        //x_2[i+31] = (char) ((int)x_2[i+3] + (int)x_2[i+2] + (int)x_2[i+1] + (int)x_2[i])%2;
    //}
    //for (int i = 0; i < N_c; i++) {
        //i_m = i+N_c;
        //x_1[i_m+31] = (char) ((int)x_1[i_m+3] + (int)x_1[i_m])%2;
        //x_2[i_m+31] = (char) ((int)x_2[i_m+3] + (int)x_2[i_m+2] + (int)x_2[i_m+1] + (int)x_2[i_m])%2;
        //c[i] = (char) ((int)x_1[i_m] + (int)x_2[i_m])%2;
    //}
    //out = c;
    return out;
}
