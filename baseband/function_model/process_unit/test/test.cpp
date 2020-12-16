#include <stdio.h>
#include <math.h>
#include <process.h>

int test()
{
    char b__q[] = {'1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0'};
    int size_bq = 20;
    int q = 1;
    int n_RNTI = 1;
    int N_ID_cell = 1;
    int n_s = 2;
    int x = 0;
    int y = 1;

    char * data ;
    int ta = scrambling(b__q, size_bq, q, n_RNTI, N_ID_cell, n_s, x, y, data);
    for (int i = 0; i < size_bq; i++) {
        printf("%c\n", *data+i);
    }
    //printf("%s\n", data);
    return 0;
}

int aa()
{
    int a = 10;
    char x = '1'; 
    int ma = a%2;
    char b = (char)ma;
    char c = (char) ((int)x + 1)%2;
    char str1[] = "10101010";
    char str2[] = {'1', '0', '1', '0', '1', '0', '1', '0'};
    char int2[] = {1, 0, 1, 0, 1, 0, 1, 0};
    printf("str1 is %s, str2 is %s\n", str1, str2);
    printf("print str2 in char:");
    for (int i = 0; i < sizeof(str2); i++) {
        printf("%c", str2[i]);
    }
    printf("\n");
    printf("print int2 in char:");
    for (int i = 0; i < sizeof(int2); i++) {
        printf("%d", int2[i]);
    }
    printf("\n");
    //printf("ma is %d\n", ma);
    //printf("b is %c\n", b);
    //printf("c is %c\n", c);
    //printf("hello\n");
    return 1;
}

int test_pseudo_generator()
{
    int c_init = (int) (pow(2, 14) + pow(2,13) +1);
    int size_bq = 20;
    CharArray c_q = pseudo_random_sequence_generation(c_init, size_bq);
    int ti = 0;
    printf("result is: ");
    for (int i = 0; i < c_q.length; i++) {
        printf("%c", *(c_q.par+i));
    }
    //while (c_q != NULL) {
        //if (ti>(1600+size_bq+10)) {
            //printf("\nError: exceed array. index is %d\n", ti);
            //return 0;
        //}
        //ti++;
    //}
    printf("\n");
    return 1;
}

int main(int argc, char *argv[])
{
    //test();
    //aa();
    test_pseudo_generator();
    return 0;
}
