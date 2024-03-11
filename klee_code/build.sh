#!/bin/bash

if [ -z "$1" ]
  then
    echo "No argument supplied"
    exit 1
fi


FILENAME=$1
clang -I ../../include -emit-llvm -c -g -O0 -Xclang -disable-O0-optnone $FILENAME