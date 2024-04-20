#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 17:06:59 2021

@author: VilleWassberg
"""

import random
import csv

def file_mishandling_function(stations, connections):
    '''
    This function is made to ensure that some expected errors can be handled 
    early in this program such that the user won't be annoyed by some later on
    errors that could have been handled already. Its main purpose is to check 
    the submitted files for some deviations.
    '''
    if stations.endswith(".csv") == False or connections.endswith(".csv") == False:
        raise TypeError('The provided files must both be csv files for this \
                        program to work properly!')
    try:
        with open(stations, 'r') as stations, open(connections, 'r') as connections:
            stations = csv.reader(stations)
            connections = csv.reader(connections)
            for row in stations:
                if len(row) != 2:
                    raise IndexError('The stations file is expected to contain\
                                     two comma separated columns')
            for row in connections:
                if len(row) != 4:
                    raise IndexError('The connections file is expected to contain\
                                     four comma separated columns')
            
    except FileNotFoundError:
        print('Please make sure to enter files that exists in the same folder\
              as this program.')
        return main()
        
def sort_train_stations_by_line(connections):
    dict_of_stations_in_same_line = {}
    try:
        with open(connections, 'r') as train_stops:
           train_stops_reader = csv.reader(train_stops)
    
           for row in train_stops_reader:
               line = row[2]
               station_a = row[0]
               station_b = row[1]
               '''Create an ordered dict from north to south with the lines as
               keys and lists of the lines' stations as values.'''
               if 'S' in row: 
                   if line not in dict_of_stations_in_same_line:
                       #If stations are connected in a southern direction, then 
                       #the order is correct and station 1 comes before station 2
                       dict_of_stations_in_same_line.update({line:[station_a, station_b]})
                   lines_stations = dict_of_stations_in_same_line[line]
                   if station_a in lines_stations and station_b not in lines_stations:
                       lines_stations.insert(lines_stations.index(station_a) + 1, station_b)
                   elif station_b in lines_stations and station_a not in lines_stations:
                       lines_stations.insert(lines_stations.index(station_b), station_a)
               elif 'N' in row:
                   #This aims to put the stations in order with north in the
                   #beginning and southern stations in the end just as the major if.
                   if line not in dict_of_stations_in_same_line:
                       dict_of_stations_in_same_line.update({line:[station_b, station_a]})
                   lines_stations = dict_of_stations_in_same_line[line]
                   if station_a in lines_stations and station_b not in lines_stations:
                       lines_stations.insert(lines_stations.index(station_a), station_b)
                   elif station_b in lines_stations and station_a not in lines_stations:
                       lines_stations.insert(lines_stations.index(station_b) + 1, station_a)
           return dict_of_stations_in_same_line
    except: 
        FileNotFoundError('Please  make sure to provide a file in the same\
                           folder as this program. ') 


def random_start_position_and_direction(sorted_stations):
    '''

    Parameters
    ----------
    sorted_stations : 
    The function takes a sorted dictionary as parameter. The dictionary is
    expected to contain a list of train stations ordered from north to south
    in the values spots and a key which represents the line that relates to
    each list of stations. 

    Returns
    -------
    Returns a tuple of random line, station an direction.

    '''
    amount_of_lines = len(sorted_stations)
    k = random.randrange(amount_of_lines)
    rand_line = list(sorted_stations)[k]
    
    amount_of_stations_in_line = len(sorted_stations[rand_line])
    l = random.randrange(amount_of_stations_in_line)
    rand_station = sorted_stations[rand_line][l]
    
    rand_direction = random.choice(('N','S'))
    
    if sorted_stations[rand_line].index(rand_station) == 0:
        #Makes sure that if the station is furthest north then the direction
        #can only be south
        rand_direction = 'S'
    elif sorted_stations[rand_line].index(rand_station) == len(sorted_stations[rand_line]):
        #And here there's only stations north of this one
        rand_direction = 'N'
    return rand_line, rand_station, rand_direction


def start_positions_for_all_trains(amount_of_trains, sorted_stations):
    '''
    Parameters
    ----------
    amount_of_trains : An integer of how many trains that will be encountered
    a starting position and direction.
    
    sorted_stations : A sorted dict of train lines as keys and a list of associated
    stations ordered from north to south as values.

    Returns
    -------
    trains_start_positions : A dictionary of trains information where which train
    it is is described as the key and the value is tuples with random line,
    station and direction.
    '''
    if amount_of_trains == 0:
        return
    trains_start_positions = {}
    for i in range(1, amount_of_trains + 1):
        trains_start_positions['Train' + str(i)] = \
            random_start_position_and_direction(sorted_stations)
    #print(trains_start_positions)
    return trains_start_positions


def driving_train(train_info, sorted_stations):
    '''

    Parameters
    ----------
    train_info : A tuple (or sequence) of three is expected with a trains information
    of which line, which station and what direction it is heading. 
    sorted_stations : A sorted dict of train lines as keys and a list of associated
    stations ordered from north to south as values.

    Returns
    -------
    A new tuple of three with updated train information when train has been driven 
    one timestep. The information is as the parameters of which line, which
    station and what direction the train is heading.

    '''
    line = train_info[0]
    station = train_info[1]
    direction = train_info[2]
    train_stations = sorted_stations[line]
    position = train_stations.index(station)
    if position == 0:
        direction = 'S'
    elif position == len(train_stations) - 1:
        direction = 'N'
    if direction == 'S':
        position += 1
    elif direction == 'N':
        position -= 1
    if position == 0:
        direction = 'S'
    elif position == len(train_stations) - 1:
        direction = 'N'

    #print(position)
    station = train_stations[position]
    return line, station, direction
    

def is_train_delayed(rand_float,train_station, stations):
    '''
    Parameters
    ----------
    rand_float : A number in [0,1] which if the number is smaller than the
    probability for delay in the stations file than the train is delayed.
    train_station : A train station which describes where a train is stationed,
    which is expected to exist in the stations file. 
    stations : a csv file which contains two columns of which column 1 describes
    which station it is and column 2 what the probability for delay at that
    station is.

    Returns
    -------
    A string which describes if there is a delay or if it is okay to drive on.

    '''
    try:
        with open(stations, 'r') as stations:
            stations_delay = csv.reader(stations)
            for row in stations_delay:
                if train_station in row:
                    possibility_of_delay = float(row[1])
                    if possibility_of_delay < rand_float:
                        return 'drive on'
                    else:
                        return 'delayed'
    except FileNotFoundError:
        print('Please  make sure to provide a file in the same\
                          folder as this program. ')
        return          

        
def new_locations(trains_start_positions, sorted_stations, stations):    
    '''
    Parameters
    ----------
    trains_start_positions :  A dictionary of trains information where which train
    it is is described as the key and the value is tuples with random line,
    station and direction.
    sorted_stations : A sorted dict of train lines as keys and a list of associated
    stations ordered from north to south as values.
    stations : a csv file which contains two columns of which column 1 describes
    which station it is and column 2 what the probability for delay at that
    station is.

    Returns
    -------
    trains_new_locations : A new dictionary of trains information where which train
    it is is described as the key and the value is tuples with random line,
    station and direction when all the train has been driven one time step.

    '''
    for train in trains_start_positions:
        rand_float = random.random()
        train_station = trains_start_positions[train][1]
        delayed_or_not = is_train_delayed(rand_float, train_station, stations)
        if delayed_or_not == 'drive on':
            trains_start_positions[train] = \
                driving_train(trains_start_positions[train], sorted_stations)
        elif delayed_or_not == 'delayed': #i.e. if train is delayed
            print('Oh no, {} is delayed!'.format(train))
    trains_new_locations = trains_start_positions
    return trains_new_locations

    
def is_train_station_reachable_in_time(train_info, time, sorted_stations):
    '''
    Parameters
    ----------
    train_info : A tuple (or sequence) of three is expected with a trains information
    of which line, which station and what direction it is heading. 
    time : This is an integer of how many time steps one wants to simulate a 
    train to see which stations it has passed during that time
    sorted_stations : A sorted dict of train lines as keys and a list of associated
    stations ordered from north to south as values.

    Returns
    -------
    reached_stations : A list of all stations the train can pass in given time
    steps, starting from current station, and does not insert the station more 
    than once even though it passes the stations several times.

    '''
    station = train_info[1]
    reached_stations = [station]
    try:
        time = int(time)
    except ValueError:
        print('You must write a number!')
    for time_unit in range(time):
        train_info = driving_train(train_info, sorted_stations)    
        station = train_info[1]
        if station not in reached_stations:
            reached_stations.append(station)
    return reached_stations


def train_info_function(trains_positions, amount_of_trains, sorted_stations, stations):
    '''
    Interaction with user about a trains information such as which station it
    is stationed at and which line and which direction it is heading.

    Parameters
    ----------
    trains_positions : A dictionary of trains information where which train
    it is is described as the key and the value is tuples with random line,
    station and direction.
    amount_of_trains : An integer of how many trains that will be used.
    sorted_stations : A sorted dict of train lines as keys and a list of associated
    stations ordered from north to south as values.
    stations : a csv file which contains two columns of which column 1 describes
    which station it is and column 2 what the probability for delay at that
    station is.

    Returns
    -------
    The function train_simulation when the ineraction with the user has been
    finished in order to go further with the main simulation.

    '''
    chosen_train = input('Which train? [1 - {}] '.format(amount_of_trains))
    try:
        if int(chosen_train) < 1 or int(chosen_train) > amount_of_trains:
            print('out of bounds')
            return train_simulation(trains_positions, amount_of_trains, sorted_stations, stations)
    except ValueError:
        print('Your train is represented by a number, hence that is what you\
              have to  wright for this to work.')
        return train_simulation(trains_positions, amount_of_trains, sorted_stations, stations)
    #print(trains_positions['Train' + chosen_train])
    if trains_positions['Train' + chosen_train][2] == 'S':
        print('Train {} is going south on the {} line and is stationed at {}\
              '.format(chosen_train, trains_positions['Train' +\
                  chosen_train][0], trains_positions['Train' +\
                  chosen_train][1]))
    elif trains_positions['Train' + chosen_train][2] == 'N':
        print('Train {} is going north on the {} line and is stationed at {}\
              '.format(chosen_train, trains_positions['Train' +\
                  chosen_train][0], trains_positions['Train' +\
                  chosen_train][1]))
    return train_simulation(trains_positions, amount_of_trains, sorted_stations, stations)    


def route_info_function(trains_positions, amount_of_trains, sorted_stations, stations):
    '''
    Parameters
    ----------
    trains_positions : A dictionary of trains information where which train
    it is is described as the key and the value is tuples with random line,
    station and direction.
    amount_of_trains : An integer of how many trains that will be used.
    sorted_stations : A sorted dict of train lines as keys and a list of associated
    stations ordered from north to south as values.
    stations : a csv file which contains two columns of which column 1 describes
    which station it is and column 2 what the probability for delay at that
    station is.

    Returns
    -------
    The function train_simulation when the ineraction with the user has been
    finished in order to go further with the main simulation.

    '''
    chosen_train = input('Which train? [1 - {}] '.format(amount_of_trains))
    try:
        if int(chosen_train) < 1 or int(chosen_train) > amount_of_trains:
            print('out of bounds')
            return train_simulation(trains_positions, amount_of_trains, sorted_stations, stations)
    except ValueError:
        print('Your train is represented by a number, hence that is what you\
              have to  wright for this to work.')
        return train_simulation(trains_positions, amount_of_trains, sorted_stations, stations)
    line = trains_positions['Train' + chosen_train][0]
    chosen_station = input('Which station?\
                           \nThis list contains the stations at the same line as\
                               your train: {} \n'\
                               .format(sorted_stations[line]))
    try:
        time = int(input('Which time span (written as a number) would you like to check?\
                 If float is given I will check nearest lower integer.\n'))
    except ValueError:
        print('You must write a number!')
        return route_info_function(trains_positions, amount_of_trains, sorted_stations, stations)
    train_info = trains_positions['Train' + chosen_train]                           
    reached_stations =  is_train_station_reachable_in_time(train_info, time,\
                sorted_stations)
    if chosen_station in reached_stations:
        print('It is possible to reach this station in time! In fact\
              , you could reach it in exactly {} time units unless delayed'.format(\
                  reached_stations.index(chosen_station)))
    else:
        print('Sorry, it is not possible to reach ' + chosen_station\
          + ' in time')
    return train_simulation(trains_positions, amount_of_trains, sorted_stations, stations)

        
def train_simulation(trains_positions, amount_of_trains, sorted_stations, stations):
    '''
    This is the interaction function that pulling all the strings of which is
    chosen by the user.

    Parameters
    ----------
    trains_positions : A dictionary of trains information where which train
    it is is described as the key and the value is tuples with random line,
    station and direction.
    amount_of_trains : An integer of how many trains that will be used.
    sorted_stations : A sorted dict of train lines as keys and a list of associated
    stations ordered from north to south as values.
    stations : a csv file which contains two columns of which column 1 describes
    which station it is and column 2 what the probability for delay at that
    station is.

    Returns
    -------
    The function calls other functions depending on the users choice. Unless
    the user want to quit the simulation, either route info, train info or
    the train simulation function itself is called.

    '''
    your_choice = input('Would you like to:\n\
       [c] continue the simulation?\n\
       [i] have some info of a train?\n\
       [r] get route info\n\
       [q] quit this simulation?\n\
        c, i, r or q? ')
    if your_choice == 'c':
        print('Driving train...')
        trains_positions = new_locations(trains_positions, sorted_stations, stations)
        return train_simulation(trains_positions, amount_of_trains, sorted_stations, stations)
    elif your_choice == 'i':
        return train_info_function(trains_positions, amount_of_trains, sorted_stations, stations)
    elif your_choice == 'r':
        return route_info_function(trains_positions, amount_of_trains, sorted_stations, stations)           
    elif your_choice == 'q':
        print('bye bye')
        return
    else:
        print('I can only accept either c, i, r or q as an answer')
        return train_simulation(trains_positions, amount_of_trains, sorted_stations, stations)  


def main():
    '''
    This is the main function which the user has to call in order to begin the 
    simulation.
    '''

    stations = input('Please provide the location of your file of stations.\n')
              
    connections = input('Please provide the location of your connections file.\n')
    
    file_mishandling_function(stations, connections)
    
    try:
        amount_of_trains = int(input('How many trains would you like to simulate?\n'))
    except ValueError:
        print('You must write a number!')
        return main()
    
    sorted_stations = sort_train_stations_by_line(connections)
    
    trains_positions = start_positions_for_all_trains(amount_of_trains, sorted_stations)

    train_simulation(trains_positions,amount_of_trains, sorted_stations, stations)
 
#Test functions

def test_sorted_stations():
    sorted_stations = sort_train_stations_by_line('connections.csv')
    stations = {'red': ['Östermalmstorg', 'T-centralen', 'Gamla stan', 'Slussen', \
         'Mariatorget', 'Zinkensdamm'], 'green': ['Hötorget', 'T-centralen',\
         'Gamla stan', 'Slussen', 'Medborgarplatsen', 'Skanstull'],\
          'blue': ['Fridhemsplan', 'Rådhuset', 'T-centralen', 'Kungsträdgården']}
    assert sorted_stations == stations
    sorted_rand_stations = sort_train_stations_by_line('randomconnections.csv')
    rand_stations = {'green': ['a', 'b', 'c'], 'white': ['c', 'z', 'y', 'x'],\
                     'blue': ['y', 'f', 'g', 'h', 'a']}
    assert sorted_rand_stations == rand_stations
    print('passed')
    
def test_driving_train():
    sorted_stations = sort_train_stations_by_line('connections.csv')
    
    train_info = ('green', 'T-centralen', 'S')
    new_pos = driving_train(train_info, sorted_stations)
    assert new_pos == ('green', 'Gamla stan', 'S')
    
    train_info = ('green', 'Medborgarplatsen', 'S')
    new_pos = driving_train(train_info, sorted_stations)
    assert new_pos == ('green', 'Skanstull', 'N')
    print('passed')
    
def test_is_reachable():
    sorted_stations = sort_train_stations_by_line('connections.csv')
    time = 2
    train_info = ('green', 'T-centralen', 'S')
    reached = is_train_station_reachable_in_time(train_info, time, sorted_stations)
    assert 'Slussen' in reached
    time = 5
    reached = is_train_station_reachable_in_time(train_info, time, sorted_stations)
    assert 'Hötorget' not in reached
    print('passed')
    
def test_some_functions():
    test_sorted_stations()
    test_driving_train()
    test_is_reachable()
    print('Wohooooo!')



