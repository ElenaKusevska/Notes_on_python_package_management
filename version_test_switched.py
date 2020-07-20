#!/usr/bin/python3.6
import inspect
import sys

print("-----------------------------------------------")
print("sys.path old:")
print(sys.path)
print("-----------------------------------------------")
print("sys.path[4] old    ", sys.path[4])
print("sys.path[6] old    ", sys.path[6])
print("-----------------------------------------------")

# Make switch:
p1 = sys.path[4]
p2 = sys.path[6]
sys.path[4] = p2
sys.path[6] = p1

print("sys.path[4] new    ", sys.path[4])
print("sys.path[6] new    ", sys.path[6])
print("-----------------------------------------------")
import numpy

print("'inspect.getfile(numpy)' gives: ", inspect.getfile(numpy))
print(" ")
print("'numpy.__version__' gives: ", numpy.__version__)
