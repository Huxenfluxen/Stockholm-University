#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 22:38:43 2021

@author: VilleWassberg
"""


def vowels_or_consonants():
    vs = "AOUÅEIYÄÖaouåeiyäö"
    outv = ""
    outc = ""
    answer = input("Vowels or consonants?")
    answer2 = input("Write a sentence")
    for v in answer2:
        if v in vs:
            outv += v
        else:
            outc += v
    if answer == 'vowels':
        return print('Vowels:', outv)
    elif answer == 'consonants':
        return print('consonants:', outc)
    elif answer == 'both':
        return print('Vowels and consonants respectively', outv, outc)
print(vowels_or_consonants())
        
    
   

        
            