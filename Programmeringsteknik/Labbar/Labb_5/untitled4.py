#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 22:53:30 2021

@author: VilleWassberg
"""

class DnaSeq:
    '''
    DnaSeq is a class for DNA sequences and it´s accession string. 
    
    Attributes
    ----------
    accession : a unique identifier of a DNA sequence.
    seq : a DNA sequence.
    '''
    def __init__(self, accession, seq):
        self.accession = accession
        self.seq = seq
        #Raise error if accession or sequence is empty.
        if not self.accession or not self.seq: 
            raise ValueError('The accession or the sequence is empty')

    def __len__(self):  #Method to calculate length of sequence.    
        return len(self.seq)
            

    def __str__(self):  #Method to print lable of accession name.
        return '<DnaSeq accession=' + str(self.accession) + '>'


def read_dna(filename):
    '''
    read_dna() reads a file with dna records and returns a list with them 
        transformed to DnaSeq objects.

    Parameters
    ----------
    filename : name of file containing records with a accession line and 
               a sequence line.

    Returns
    -------
    dna_list : List of DnaSeq-objects from the file.

    '''
    with open(filename) as h:
        dna_list = []
        for row in h.readlines(): 
            row = row.strip()   #Erase blank lines and newline characters.
            
            if not len(row) > 0:  #If row is empty
                continue            
            elif row[0] == '>':   #If row starts with a '>' row is the accession.          
                dna_accession = row[1: ]
            else:   #Else row is the sequence, classify as DnaSeq and append to list.
                dna_sequence = row
                dna_list.append(DnaSeq(dna_accession, dna_sequence))
   
        return dna_list
            


def check_exact_overlap(dna_object1, dna_object2, min_length = 10):
    '''
    check_exact_overlap() takes two DnaSeq-objects and checks for overlaps of 
        the sequences considering a minimum lenght. 

    Parameters
    ----------
    dna_object1 : the first DnaSeq-object.
    dna_object2 : the second DnaSeq-object that function checks if overlaps the first.
    min_length : the minimum overlap length to look for. The default is 10.

    Returns
    -------
    Returns the length of the overlap. If overlap is shorter than minimum 
        overlap length or the minimum length is 0 the function returns 0.

    '''
    #Extract the sequences form the DnaSeq-objects.
    dna_seq1 = dna_object1.seq
    dna_seq2 = dna_object2.seq
    
    for index in range(0, len(dna_seq1)):
        #Check overlap with start from index to end of sequence.
        if dna_seq1[index:] == dna_seq2[0 : len(dna_object1) - index]:
           
            #If overlap is shorter than minimum overlap length/the minimum length is 0.
            if len(dna_seq1[index:]) < min_length or min_length == 0:
                return 0                
                break                
            else: #Else return the overlap length.
                return len(dna_seq1[index: ])
                break
    return 0


def overlaps(dna_list, overlap_function):
    '''
    overlaps() detects overlaps among pairs of sequences in the input list 
        using the overlap function. 

    Parameters
    ----------
    dna_list : list of DnaSeq-objects.
    overlap_function : name of function that checks overlap between two 
                       DnaSeq-objects sequences and returns overlap length.

    Returns
    -------
    d : a nested dictionary with the overlap between a pair of DnaSeq-objects 
        sequences. The accessions of the objects acts as keys and the overlap 
        as value.

    '''
    d = {}
    for index, dna_object in enumerate(dna_list):
        dna_obj1 = dna_list.pop(index) #Pop object from list.

        for dna_obj2 in dna_list: #Check overlap between the DnaSeq-objects.
            overlap = overlap_function(dna_obj1, dna_obj2)       
            
            if overlap > 0: #If overlap is greater than 0 append to dictionary.
                d[dna_obj1.accession] = {dna_obj2.accession : overlap}
       
        dna_list.insert(index, dna_object) #Insert back pop object in same place.
        
    return d


#-----------------------------------------------------------------------------        
#
# Testing code
#
def test_class_DnaSeq():
    s1 = DnaSeq('s1', 'ACGT')
    s2 = DnaSeq('s2', 'ATGTTTGTTTTTCTTGTTTTATTGCCACTAGTCTCTAGTCAGTGTGTTAATCTTACAACCAGAACTCAAT')
    assert len(s1) == 4, 'Your length method (__len__) is not correct.'
    assert len(s2) == 70, 'Your length method (__len__) is not correct.'

    assert str(s1) == '<DnaSeq accession=s1>', 'The __str__ method is not following the specification.'
    assert str(s2) == '<DnaSeq accession=s2>', 'The __str__ method is not following the specification.'

    # The rest of this function is verifying that we are indeed raising an exception.
    status = 0
    try:
        s3 = DnaSeq('', 'ACGT')
    except ValueError:
        status += 1
    try:
        s3 = DnaSeq('s3', None)
    except ValueError:
        status += 1

    try:
        s3 = DnaSeq(None, '')
    except ValueError:
        status += 1
    if status != 3:
        raise Exception('class DnaSeq does not raise a ValueError '
                        'exception with initialised with empty '
                        'accession and sequence.')
    print('DnaSeq passed')

def test_reading():
    dna1 = read_dna('ex1.fa')
    assert len(dna1) == 6, 'The file "ex1.fa" has exactly 6 sequences, but your code does not return that.'
    assert list(map(lambda x: x.accession, dna1)) == [f's{i}' for i in range(6)], 'The accessions are not read correctly'
    print('read_dna passed')

def test_overlap():
    s0 = DnaSeq('s0', 'AAACCC')
    s1 = DnaSeq('s1', 'CCCGGG')
    s2 = DnaSeq('s2', 'TTTTCC')
    data1 = [s0, s1, s2]
    assert check_exact_overlap(s0, s1, 2) == 3
    assert check_exact_overlap(s0, s1) == 0
    assert check_exact_overlap(s1, s2, 2) == 0
    assert check_exact_overlap(s2, s1, 2) == 2

    res0 = overlaps(data1, lambda s1, s2: check_exact_overlap(s1, s2, 2))
    assert len(res0) == 2, 'You get the wrong number of overlaps'
    assert res0 == {'s0': {'s1': 3}, 's2': {'s1': 2}}

    dna_data = read_dna('ex1.fa')
    res1 = overlaps(dna_data, check_exact_overlap)
    assert len(res1) == 5
    for left, right in [('s0', 's1'), ('s1', 's2'), ('s2', 's3'), ('s3', 's4'), ('s4', 's5')]:
        assert res1[left][right], f'Missing overlap of {left} and {right} (in that order)'
    print('overlap code passed')

def test_all():
    test_class_DnaSeq()
    test_reading()
    test_overlap()
    print('Yay, all good')