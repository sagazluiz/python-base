#!/usr/bin/env python3
import os
import sys

# EAFP - Easy to ASK Forgiveness than Permission

try:
    raise RuntimeError("An error ocurred duing the execution time")

try:
    names = open("names.txt").readlines() # FileNotFoundError
    1 / 1 # ZeroDivisionError
    print(names.append) # AttributeError
except FileNotFoundError as e: # Bare Except
    print(f"[Error] {str(e)}")
    sys.exit(1)
    # retry -- pode ser feito com função recursiva ou while
except ZeroDivisionError:
    print("You can not divide per zero")
    sys.exit(1)
except AttributeError:
    print("List does not has banana")
    sys.exit(1)    
try: 
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
