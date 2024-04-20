#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 18:10:31 2021

@author:
"""

'''This function takes the name of a file and creates an empty dictionairy as 
well as calls the two functions "collect_data" and "execution" in order to handle 
the given data in provided file and returns the average of the measurements. 
The file is supposed to be a comma separated file of for columns where each column 
is; batch, x values, y values, measurement value, in order. The returned values 
are the average of all the measurements taken within the unit circle.
The function has been changed to be able to provide information of an event when
given file could not be found, with try and except statements.'''

def get_average_of_data(filename):
    data = {}
    try:
        with open(filename, 'r') as h:
            data = collect_data(h, data)
            sorted_data = dict(sorted(data.items()))
            execution(sorted_data)
    except FileNotFoundError:
        print('Sorry, seems like the file ' + str(filename) + ' does not exist in the same folder as this program.')
        
'''This function takes an opened file and a dictionairy, and returns a data set 
in form of a dictionairy with the information extracted from the file. The function 
has been changed to be able to handle eventual typos such as letters instead of
 numbers inside the data sheet, with try and except statements. Which makes the 
 function continue with what's left.'''
 
def collect_data(file, data):
    for line in file:
        four_vals = line.split(',')
        batch = four_vals[0]
        if not batch in data:
            data[batch] = []
        try:
            data[batch] += [(float(four_vals[1]), float(four_vals[2]), float(four_vals[3]))] # Collect data from an experiment
        except ValueError:
            print('Sorry, it seems like one of the columns in batch ' + str(batch) + ' is not entirely a number and is therefore not included.')
    return data
    
'''This function takes a dictionairy data set as argument and loops through its keys and 
values, and  calls the "calculation_of_average" function to be able to spit out the
average values calcaluated in it. 
The function has been changed to be able to handle 
eventual data taken outside the unit circle, hence zero division, with try and except statements.'''

def execution(data):
    for batch, sample in data.items():
        if len(sample) > 0:
            try:
                average = calculations_of_average(sample)
                print(batch,"\t", average)
            except ZeroDivisionError:
                print('Sorry, the given data in batch ' + str(batch) + ' might be captured from outside the unit circle. ')
        else:
            print(batch, "\tNo data")
    
'''This function makes the calculations of the average from a list of tuples
with 3 elements which the first element is x coordinates, second is the y 
coordinates and third the value of the measurement data, as long as the x and y 
coordinates are within the unit circle'''

def calculations_of_average(sample):
    number_of_measurements = 0
    sum_of_measurements = 0
    for (x, y, value) in sample:
        if x**2 + y**2 <= 1:
            sum_of_measurements += value
            number_of_measurements += 1
    average = sum_of_measurements/number_of_measurements
    return average

'''Runs the code from "get_average_of_data" for chosen file'''

filename = input('Which data file? ')
print(get_average_of_data(filename))

#Borde kanske ha gjort en:
#def main():
    #filename = input('Which data file? ')
    #print(get_average_of_data(filename))
