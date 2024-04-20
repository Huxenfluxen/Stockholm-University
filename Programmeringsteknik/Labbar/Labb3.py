#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 15:53:01 2021

@author: 
"""
'''Uppgift 1 a)'''
'''This function aims to put in a value "x" into a list ordered by size'''
def insert_in_sorted(x,sorted_list):
    if sorted_list == []:
        return [x]
    for k in sorted_list:
        if k >= x :
            i = sorted_list.index(k)
            sorted_list.insert(i,x)
            return sorted_list
    else:
        sorted_list.append(x)
        return sorted_list
'''Uppgift 1 b)'''
'''This function aims to sort a given list into a list ordered by size'''
def insertion_sort(my_list):
    out = []
    for elem in my_list:
         out = insert_in_sorted(elem, out)
    return out

'''Uppgift2 a)'''
'''This function aims to count the amount of rows within a given textfile'''
def count_rows(f):
    try:
        with open(f,'r') as text:
            rows = text.readlines()
        return len(rows)
    except FileNotFoundError:
        print('Not able to open the file;' + ' ' + f + '. ' + 'Plaese make sure the file is saved in the same map as the function.')

'''Uppgift 2 b)'''
'''This function aims to output a textfile similar to the input textfile but 
which row each line is in as well as how many characters up to that point'''
def annotate(f):
    try:
        with open(f,'r') as text_in, open('annotate.txt', 'w') as text_out:
            i = 0
            words = 0
            for line in text_in:
                words += len(line.split(' '))
                the_line = line.split("\n")
                the_line_string = ''
                for word in the_line:
                    the_line_string += word
                text_out.write(the_line_string + ' ' + str(i) + ' ' + str(words) + '\n')
                i += 1
        h = open('annotate.txt')
        print(h.read())
        h.close()
    except FileNotFoundError:
        print('Not able to open the file;' + ' ' + f + '. ' + 'Plaese make sure the  file is saved in the same map as the function.')
                
                    
'''Uppgift 3 a)'''
'''This function aims to provide the user with which row a given string of words
 is written in.'''
hinfile = open('infile.txt')
sinfile = 'I'
def find_matching_lines(h, s):
    i = 0
    matching_lines = []
    for line in h:
        if s in line:                
                matching_lines.append((i, line.splitlines()))
        i +=1
    return matching_lines


    
'''Uppgift 3 b)'''
'''This function aims to provide the user with which row a given string of words
 is written in when given a certain file to look within.'''
def findlines():
    try:
        file_name = input('Please write the name of the file you want to find lines for')
        your_string = str(input('Please write the words you want to search within the file for'))
        with open(str(file_name)) as hinfile:
            found_lines = find_matching_lines(hinfile, your_string)
        return found_lines
    except FileNotFoundError:
        print('Not able to open the file;' + ' ' + file_name + '. ' + 'Plaese make sure the  file is saved in the same map as the function.')


'''Uppgift 4 a)'''
'''This function aims to provide the user a dictionairy with pairs of row number
and line'''
def save_rows(h):
    i = 0
    my_dict = {}
    for line in h:
        for k in line.splitlines(): 
            my_items = {i: k}
            my_dict.update(my_items)
        i += 1
    return my_dict

'''Uppgift 4 b)'''
'''This function aims to provide the user the ability to print the string within
 chosen file by only given coordinates, i.e. row number and column number.'''
def main():
   try:
       infile = input('Please write the name of your file.')
       with open(str(infile)) as new_file:
           indexed_file =  save_rows(new_file)
           while True:
               row = input('Which row do you want to use? Starting from zero.')
               if row == 'exit':
                   return
               elif int(row) > len(indexed_file):
                   raise ArithmeticError("Out of bounds")
               your_line = indexed_file[int(row)]
               col = input('Which column do you want to use? Starting from zero.')
               if col == 'exit':
                   return
               elif int(col) > len(your_line):
                   raise ArithmeticError("Out of bounds")
    
               your_string = your_line[int(col)]
               if your_string == ' ':
                   print('Space')
                   
               print(your_string)
   except FileNotFoundError:
        print('Not able to open the file;' + ' ' + infile + '. ' + 'Plaese make sure the  file is saved in the same map as the function.')
   










