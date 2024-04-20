#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 18:54:23 2021

@author: VilleWassberg
"""

def drop_zeroes(p_list):
    i = len(p_list)
    while p_list[i-1] == 0:
        x = p_list.pop()
        print('Your', str(i)+'th','index dropped:', x)
        i -= 1
    print('Your new p_list:',p_list)
    return p_list

def pal_poly(p_list,x):
    degree = 0
    p=0
    # Collect a list of terms
    for coeff in p_list:
        p += coeff*(x**degree)
        degree += 1
    return p



def added_poly(p_list,q_list):
    the_added_poly = []
    i = len(p_list)
    j = i
    k = len(q_list)
    l = k
    pq_list = p_list + q_list
    while j > len(the_added_poly) or l > len(the_added_poly):
        m = pq_list[j-i]
        n = q_list[j+l-k]
        i-=1
        k-=1
        
        the_added_poly.append(m+n) 
    return the_added_poly