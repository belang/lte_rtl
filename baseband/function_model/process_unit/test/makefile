
CPP = g++

s_include = ..
source = ../pseudo_random_sequence_generation.c test.c
#source = ../pseudo_random_sequence_generation.c ../scrambling.c test.c
target = test.exe

default: all

a:
	gcc test.c -o a.exe

c:
	gcc -I ${s_include} ${source} -o pseudo_random_sequence_generation.o

all:
	gcc -I ${s_include} ${source} -o ${target}
	./${target}

compile:
	gcc -I -c -o

linke:
	gcc -I -c -o

debug:
	gcc -g -I ${s_include} ${source} -o ${target}

share:
	gcc -shared -I ${s_include} ${source} -o pseudo_random_sequence_generation.o
