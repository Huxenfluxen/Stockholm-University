#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 15:21:45 2021

@author: VilleWassberg
"""

def drop_zeroes(p_list):
    if p_list == []:
        return p_list
    while p_list[-1] == 0 and p_list !=[]:
        x = p_list.pop()
        print(x)
        if p_list == []:
            break
    return p_list
        
        