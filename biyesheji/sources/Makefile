CC := gcc
INC_FLAG= ../headers/
OBJ_DIR= ./objs/

.PONY:all
all:console.o module.o

console.o: console.cc $(INC_FLAG)console.h
	$(CC) -c console.cc -o $(OBJ_DIR)console.o

module.o: module.cc $(INC_FLAG)module.h
	$(CC) -c module.cc -o $(OBJ_DIR)module.o



