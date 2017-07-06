# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:13:07 2017
@author: dexter

Loops are control structures that iterate over a range to perform a certain task.

There are two kinds of loops in Python.

A for loop:

for i in range(0, 5):
    print i

And a while loop:

i = 0
while i < 5:
    print i
    i += 1

Note Be careful about indentation in Python.
"""

if __name__ == "__main__":
    n = int(raw_input())
    if 1 <= n <=20:
        for i in range(0,n):
            print i*i
            i +=1
    
