#!/usr/bin/python

from sys import argv
from ioc import *

filename = argv[1]

ioc = IOC()

ioc.importFile(filename)

print(ioc.getPackage())

