# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 11:11:24 2023

@author: ville
"""
import time

def diff_squares(N):
    
    for i in range(100000000):
        
        
        if ((N+i**2)**(0.5)).is_integer() == True:
            P = (N+i**2)**0.5 + i
            Q = (N+i**2)**0.5 - i
    
        else:
            continue
    return (P,Q)

start = time.time()

print(diff_squares(52907))

end = time.time()

print(end-start)





    

        