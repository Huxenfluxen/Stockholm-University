#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 09:15:45 2021

@author:
"""

# Sample data:
# 1, 0.1, 0.2, 73
# 1, 0.11, 0.1, 101
# 2, 0.23, 0.01, 17
# 2, 0.12, 0.15, 23
#
# Pretend this is taken from two (or more) different experiments: batch 1 and batch 2.
# Columns are:
#   batch number
#   x coordinate
#   y coordinate
#   measurement
            


filename = input('Which data file? ')

data = dict()               # Or data = {}
with open(filename, 'r') as h:
    for line in h:
        four_vals = line.split(',')
        batch = four_vals[0]
        if not batch in data:
            data[batch] = []
        data[batch] += [(float(four_vals[1]), float(four_vals[2]), float(four_vals[3]))] # Collect data from an experiment
            
for batch, sample in data.items(): 
    if len(sample) > 0:
        n = 0
        x_sum = 0
        for (x, y, val) in sample:
            if x**2 + y**2 <= 1:
                x_sum += val
                n += 1
        average = x_sum/n
        print(batch, "\t", average)
    else:
        print(batch, "\tNo data")