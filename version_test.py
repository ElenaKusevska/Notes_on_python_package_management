#!/usr/bin/python3.6
import numpy
import inspect
import sys

print("-----------------------------------------------")
print("sys.path:")
print(sys.path)
print("-----------------------------------------------")
print("'inspect.getfile(numpy)' gives: ", inspect.getfile(numpy))
print(" ")
print("'numpy.__version__' gives: ", numpy.__version__)
print("-----------------------------------------------")
