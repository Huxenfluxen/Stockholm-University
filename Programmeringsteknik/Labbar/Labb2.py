#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 11:24:53 2021

@author: 
"""
#Uppgift 1
p = [2, 0, 1]
q = [-2, 1, 0, 0, 1]

def poly_to_string(p_list):
    
    if p_list == []:
        return '0'
    '''
    Return a string with a nice readable version of the polynomial given in p_list. Can only accept number elements.
    '''
    terms = []
    degree = 0

    # Collect a list of terms
    for coeff in p_list:
        if coeff == 0:
            pass
        elif degree == 0:
            terms.append(str(coeff))
        elif coeff == 1 and degree == 1:
            terms.append('x')
        elif degree == 1:
            terms.append(str(coeff) + 'x')
        elif coeff == 1 and degree > 1:
            terms.append('x^' + str(degree))
        else:
            term = str(coeff) + 'x^' + str(degree)
            terms.append(term)        
        degree += 1
        
    final_string = ' + '.join(terms) # The string ' + ' is used as "glue" between the elements in the string
    if terms == []:
        final_string = '0'
    return final_string

#Uppgift 2
p0 = [1,2,0,1,0,0,0]
p1 = [0,0,0]
p2 = [0,9,8,0,6,4,0,0]
'''
Return a list of the elements of the input list minus all the ending zeros. Can only accept number elements.
'''
def drop_zeroes(p_list):
    if p_list == []:
        return p_list
    while p_list[-1] == 0 and p_list !=[]:
        x = p_list.pop()
        print(x)
        if p_list == []:
            break
    return p_list

#Uppgift 3
v0=[1,3,4,0,0,0]
v=[1,3,4,0]
u0=[4,3,5,76,45,32,0,0,0,0,0,0]
u=[4,3,5,76,45,32]
'''
Return 'True' or 'False' whether the two input lists/polynomials are equal. Can only accept number elements.
'''
def eq_poly(p_list,q_list):
    p_list = drop_zeroes(p_list)
    q_list = drop_zeroes(q_list)
    print(p_list, q_list)
    return p_list == q_list

#Uppgift 4
'''
Return the value of a polynomial in the point x. Can only accept number elements.
'''
def eval_poly(p_list,x):
    degree = 0
    p=0
    # Collect a list of terms
    for coeff in p_list:
        p += coeff*(x**degree)
        degree += 1
    return p

#Uppgift 5
# a)
'''
Returns the negation of the polynomial. Can only accept number elements in a list.
'''
def neg_poly(p_list):
    the_neg_poly=[]
    for coeff in p_list:
        coeff=-coeff
        the_neg_poly.append(coeff)
    return the_neg_poly

#b)
'''
Hittar inte felet...... darfor kommer det aven bli fel pa 5 c).
    returns the sum of the to input lists
'''
def add_poly(p_list,q_list):
    the_added_poly = []
    i = len(p_list)
    j = i
    k = len(q_list)
    l = k
    if i > k:
        while k > 0:
            coeff = p_list[l-k]+q_list[l-k]
            the_added_poly.append(coeff)
            k -= 1
        while k == 0 and i > l:
            coeff = p_list[j-i+l]
            the_added_poly.append(coeff)
            i-=1
    elif k > i:
        while i > 0:
            coeff = p_list[i-1]+q_list[i-1]
            the_added_poly.insert(i-1,coeff)
            i -= 1
        while i == 0 and k > j:
            coeff = q_list[k-1]
            the_added_poly.insert(j,coeff)
            k-=1
    else:
        while i > 0:
            coeff = p_list[i-1]+q_list[i-1]
            the_added_poly.insert(i-1,coeff)
            i -= 1
    return the_added_poly

#c)
'''
returns the subtraction of q_list from p_list; i.e. argument1 - argument2
'''

def sub_poly(p_list,q_list):
    neg = neg_poly(q_list)
    return add_poly(p_list,neg)





