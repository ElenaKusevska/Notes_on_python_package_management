#!/bin/bash

echo " "
echo "Running ./version_test.py..."
echo " "
./version_test.py

echo " "
echo "-----------------------------------------------"
echo "setting PYTHONPATH=/usr/lib/python3/dist-packages: $ PYTHONPATH ..."
echo "-----------------------------------------------"
echo " "
PYTHONPATH=/usr/lib/python3/dist-packages:$PYTHONPATH
export PYTHONPATH

echo " "
echo "Running ./version_test.py..."
echo " "
./version_test.py

