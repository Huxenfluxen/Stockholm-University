#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 15:54:10 2022

@author: VilleWassberg
"""

import unittest
import Projekt_tåg
class TestTrainProject(unittest.TestCase):
    
    def test_sorted_stations(self):
       sorted_stations = Projekt_tåg.sort_train_stations_by_line('connections.csv')
       stations = {'red': ['Östermalmstorg', 'T-centralen', 'Gamla stan', 'Slussen', \
                'Mariatorget', 'Zinkensdamm'], 'green': ['Hötorget', 'T-centralen',\
                'Gamla stan', 'Slussen', 'Medborgarplatsen', 'Skanstull'],\
                 'blue': ['Fridhemsplan', 'Rådhuset', 'T-centralen', 'Kungsträdgården']}
       self.assertEqual(sorted_stations, stations)
if __name__ == '__main__':
    unittest.main()