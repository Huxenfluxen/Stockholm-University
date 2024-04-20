#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 13:42:51 2021

@author: VilleWassberg
"""

def newton_raphson(f, f_prime, x, precision=0.001):
    ready = False
    iterations = 0
    while not ready and iterations < 100:
        x_next = x - f(x)/f_prime(x)      # Main line of code to be repeated
        ready = abs(x-x_next) < precision # Test for stopping criterion
        x = x_next                        # Preparing the next iteration
        iterations += 1
    if iterations < 100:
        return x_next
    else:           
        raise Exception('Did not converge!')