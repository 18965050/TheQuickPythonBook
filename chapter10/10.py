import sys
print(sys.path)

from modtest import *
print(f(3))

from modtest import _g
print(_g(3))

