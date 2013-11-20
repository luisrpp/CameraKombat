#!/bin/sh

# For MAC OS X
g++ -shared -Wl,-install_name,libmog2.so `pkg-config --cflags opencv` -o libmog2.so -fPIC mog2.cpp `pkg-config --libs opencv`

