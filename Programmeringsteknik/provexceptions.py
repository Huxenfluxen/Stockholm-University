#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 14:01:59 2021

@author: VilleWassberg
"""

def main():
    while True:
        parameters = input('Give parameters a, b, c for ax^2+bx+c')
        a_s, b_s, c_s = parameters.split(',')
        a=float(a_s)
        b=float(b_s)
        c=float(c_s)
        
    except Exception as e:
        print('User interaction error',e)
        continue
        fcn = lambda x: a*x*x+b*x+c
        derivative = lambda x: 2*a*x + b
        print(f'polynomial: {a}*x^2 + {b}*x + {c}')

        try:
            root = newton_raphson(fcn, derivative, 1)
            print(f'Root in x = {root}')
            print()
        except:
            print('ooooops')