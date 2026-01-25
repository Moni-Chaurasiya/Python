# from first import moni # type: ignore
import os
import sys
import first
from importlib import reload

# moni(5)
print(os.getcwd())
print(sys.platform)
print(first.moni(5))

# if we made any change in first.py file after importing first in this file then it will not track as binary is already created at the time of importing.
# Therefore we use -->> from importlib import reload
reload(first)  

for c in "moni":
    print(c)
     

# python compile to Byte Code  --->> low level & Platform Independent
# Byte code runs faster
# .pyc  --> compiled python (Frozen Binaries) --> sometime it delete also or reconstruct too or sometime it build version too 
#  __pycache__  ----->>>> it is system code is generated to organize compiled code
# Source Change & Python Version 
# first.cpython-313.pyc  --> work only for imported files -->> not for top level files

# Python Virtual Machine (PVM)
# Code loop to iterate byte Code
# Run time Engine
# Also known as python interpreter

# Byte code is not a machine code
# Python specific interpretation --> cpython, jython, Iron Python, Stackless, PyPy
# cpython --> standard implementation





