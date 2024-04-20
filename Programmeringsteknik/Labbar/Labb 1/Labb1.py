#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 15:59:52 2021

@author: 
"""
def temperature_converter():
    
    # Equation representing the conversion of temperature from fahrenheit to celsius
    def fahrenheit_to_celsius(t):
        t_celsius = (t-32)/1.8
        return t_celsius
    
    # Equation representing the conversion of temperature from celsius to fahrenheit       
    def celsius_to_fahrenheit(t):
        t_fahrenheit = t*1.8+32
        return t_fahrenheit
    
    # Equation representing the conversion of temperature from fahrenheit to both celsius and kelvin
    def fahrenheit_to_celsius_and_kelvin(t):
        t_celsius = (t-32)/1.8
        t_kelvin = t_celsius + 273.15
        return t_celsius, t_kelvin
       
    # This function provides the user the ability to make an input 
    def user_choice():
        print('Alternatives:')
        print('a. Convert Fahrenheit to Celsius')
        print('b. Convert Celsius to Fahrenheit')
        print('c. Convert Fahrenheit to both Celsius and Kelvin')
        answer = input('Which convertion do you want to do? a, b or c? ')
    
    # If the user choose "a" then the conversion from F to C is chosen, and the user is expected to provide a temperature in F.
        if answer == 'a':
            answer2 = input('Please write your choice of temperature in Fahrenheit: ')
            print(answer2)
            t = fahrenheit_to_celsius(float(answer2))
            return print("Celsius: ", t)
    
    # If the user choose "b" then the conversion from C to F is chosen, and the user is expected to provide a temperature in C.    
        elif answer == 'b':
            answer2 = input('Please write your choice of temperature in Celsius: ')
            print(answer2)
            t = celsius_to_fahrenheit(float(answer2))
            return print("Fahrenheit: ", t) 
    
    # If the user choose "c" then the conversion from F to C and K is chosen, and the user is expected to provide a temperature in F.  
        elif answer == 'c':
            answer2 = input('Please write your choice of temperature in Fahrenheit: ')
            t1, t2 = fahrenheit_to_celsius_and_kelvin(float(answer2))
            return print("Celsius, Kelvin: ", t1, t2)
    
    # If something else than a, b or c is chosen then the message below is given. 
        elif answer != ('a' or 'b' or 'c'):
            print('The function does not support the input you chose. Please try again and choose either "a", "b" or "c"')
    print(user_choice())
print(temperature_converter())
