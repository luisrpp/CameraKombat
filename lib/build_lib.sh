#!/bin/sh

# For Linux/MAC OS X
g++ -shared `pkg-config --cflags opencv` -o libmog2.so -fPIC mog2.cpp `pkg-config --libs opencv`

