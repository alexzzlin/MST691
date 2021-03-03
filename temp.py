# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re

hand=open('regex_sum_95936.txt')
numlist = list()
for line in hand:
    line = line.strip()
    stuff= re.findall('[0-9]+',line)
    if len(stuff) !=1: continue
    num=float(stuff[0])
    numlist.append(num)
print('summing:',sum(numlist))
