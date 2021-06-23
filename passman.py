import sys

from Console import Console
from Command import Command

#if exactly 2 arugments (arg[0] = python, arg[1] = passman.py)
#are in the terminal the program goes into the conolsen class
#if there are more arguments it goes to the commando class

if len(sys.argv) == 1:
    Console().process()
else:
    Command().process()
