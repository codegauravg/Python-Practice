# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:09:02 2017

@author: dexter

Without the __future__ stuff, both print statements would print 1.
The internal difference is that without that import, 
/ is mapped to the __div__() method, while with it, __truediv__() is used. 
(In any case, // calls __floordiv__().)

"""

from __future__ import division
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print a//b
    print a/b
