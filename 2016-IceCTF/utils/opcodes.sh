#!/usr/bin/env bash

# usage: ./opcodes.sh dup2-execve

prog=$1

nasm -felf64 $prog.asm -o $prog.o
ld -o $prog $prog.o
objdump -d $prog | tr '[:blank:]' '\n' | egrep '^[0-9a-f]{2}$' | sed 's#^#\\x#' | paste -s -d ''
