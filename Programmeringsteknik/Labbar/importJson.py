#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 11:26:41 2021

@author: VilleWassberg
"""

import json
legends = [ ['Lovelace', 'Ada', 1815]
          , ['Babbage', 'Charles', 1791]
          , ['Beurling', 'Arne', 1905]]
# Skapa datafil:
with open('legends.json', 'w') as outfile:
    outfile.write(json.dumps(legends))
# Senare... Skriv ut födelsesår:
with open('legends.json', 'r') as data_h:
    external_data = json.load(data_h)  
    for x in external_data:
        print(x[2]) 
