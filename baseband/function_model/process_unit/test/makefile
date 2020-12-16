

s_include = ..
source = ../pseudo_random_sequence_generation.cpp ../scrambling.cpp test.cpp
target = test.exe

default: all

a:
	g++ test.cpp -o a.exe

c:
	gcc -I ${s_include} ${source} -o ${target}

all:
	g++ -I ${s_include} ${source} -o ${target}
	./${target}

compile:
	g++ -I -c -o

linke:
	g++ -I -c -o

debug:
	g++ -g -I ${s_include} ${source} -o ${target}

