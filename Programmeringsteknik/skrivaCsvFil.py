#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv

stationer = ['Östermalmstorg',0.1],['T-centralen', 0.2], ['Slussen', 0.15], ['Gamla stan', 0.2], ['mariatorget', 0.08], ['Zinkensdamm', 0.08]



with open('stations.csv', 'w', encoding='UTF8', newline='') as h:
    
    writer = csv.writer(h)
    for i in stationer:
            
        writer.writerow(i)
    
    