#!/bin/env python

x = -12
y = 420

for i in range(x, y):
    if i >= 0 and i == int(str(i)[:: -1]):
        print i
