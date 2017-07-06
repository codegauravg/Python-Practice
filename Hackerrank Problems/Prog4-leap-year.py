# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:25:36 2017

@author: dexter

To identify Leap Year.

"""

def is_leap(year):
    leap = False
    
    #Logic for Leap Year. Year%400==0
    if year % 400 == 0:
        leap = True

    return leap

year = int(raw_input())
if 1900 < year < 100000:
    print is_leap(year)
    
else:
    print "Please enter an year greater than 1900 and less than 5 times 10."