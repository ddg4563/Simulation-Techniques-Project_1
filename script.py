#!/usr/bin/python

import sys
import random

print '\nNumber of arguments: ', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

rngseed = int(sys.argv[1])
duration = int(sys.argv[2])
numlanes = int(sys.argv[3])
car = int(sys.argv[4])
csr = int(sys.argv[5])
