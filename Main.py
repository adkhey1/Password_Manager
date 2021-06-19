import sys

from Console import Console
from Command import Command

if len(sys.argv) == 1:
    Console().process()
else:
    Command().process()
