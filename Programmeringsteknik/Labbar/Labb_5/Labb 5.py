#!/usr/bin/env python3
# -*- coding: utf-8 -*-



class DnaSeq:
    '''This class is made of an constructor __init__, and defines three methods for
returning length, a string as well as raising an error if there's a call for the
class with empty inputs. The accession acts as an identifier for the DNA sequence.'''
    def __init__(self, accession, seq):
        self.accession = accession
        self.seq = seq
        if not self.seq or not self.accession: #Uses Boolian values for empty strings and such.
            raise ValueError('Either no accesion or sequence were found')

    def __len__(self):
        return len(self.seq)

    def __str__(self):
        string = '<DnaSeq accession='+str(self.accession)+'>'
        return string
   

def read_dna(filename):
    '''This function takes an input as a file of records with accessions and DNA sequences. 
It ignores empty lines length(line) == 1. It is "cleaning up" the file by removing
certain signs and spaces. The function returns a list of the clean records.'''
    
    list_of_records = []
    with open(filename, 'r') as my_file:
        valid_letters = ['A', 'C', 'G', 'T']
        
        for line in my_file:
            if len(line) == 1:
                continue
            
            elif '>' in line:
                accession = ''
                for letter in line:
                    if letter == '>' or letter == '\n':
                        continue
                    else:
                        accession += letter

            else:
                seq = ''
                for letter in line:
                    if letter not in valid_letters:
                        continue
                    else:
                        seq += letter
                list_of_records.append(DnaSeq(accession, seq))
        return list_of_records



def check_exact_overlap(sequence1, sequence2, length = 10):
    '''This function aims to check how much sequence1 overlaps sequence2. It is
not commutative. If sequence1 ends with the same sequence as 
sequence2 begins with, then the function returns the length of that overlap.
The user can choose the minimum length to check. If the overlap is less than
chosen length then the function returns 0. The length is by default 10 but can 
be changed by the user.'''
    if sequence1.seq == sequence2.seq:
        return len(sequence1)#Then the program does not have to loop through the entire sequences.
    n = len(sequence1)
    for overlap in range(n):
        if sequence1.seq[overlap:] == sequence2.seq[:n - overlap]:
            if n - overlap >= length:
                return n - overlap
            else:
                return 0
        elif sequence1.seq[overlap:] != sequence2.seq[:n - overlap]:
            if n - overlap >= length:
                continue
            else:
                return 0



def overlaps(list_of_seq_obj, overlaps_fkt):
    '''This higher order function aims to take a list of objects with DNA sequences 
and a function, which checks for overlaps, as arguments. The function aims to 
return a dictionary of the object as a key and another dictionary with all
other objects which it overlaps with as the value.'''

    dict_of_overlaps = {}
    for seq_1 in list_of_seq_obj:
        seq_1_overlaps = {}
        for seq_2 in list_of_seq_obj:
            if seq_1.accession != seq_2.accession:
                the_overlap = overlaps_fkt(seq_1,seq_2) 
                if the_overlap != 0 and seq_2.accession not in dict_of_overlaps:
                    seq_1_overlaps.update({seq_2.accession: the_overlap})
        if seq_1_overlaps:
            dict_of_overlaps.update({seq_1.accession: seq_1_overlaps})
    return dict_of_overlaps

#
# Testing code. You should not change any line after this one!
#
def test_class_DnaSeq():
    s1 = DnaSeq('s1', 'ACGT')
    s2 = DnaSeq('s2', 'ATGTTTGTTTTTCTTGTTTTATTGCCACTAGTCTCTAGTCAGTGTGTTAATCTTACAACCAGAACTCAAT')
    assert len(s1) == 4, 'Your length method (__len__) is not correct.'
    assert len(s2) == 70, 'Your length method (__len__) is not correct.'

    assert str(s1) == '<DnaSeq accession=s1>', 'The __str__ method is not following the specification.'
    assert str(s2) == '<DnaSeq accession=s2>',           'The __str__ method is not following the specification.'

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
   s3 = DnaSeq('s3', 'CCAGGG')
   data1 = [s0, s1, s2, s3]
   assert check_exact_overlap(s0, s1, 2) == 3
   assert check_exact_overlap(s0, s1) == 0
   assert check_exact_overlap(s0, s3, 2) == 2
   assert check_exact_overlap(s1, s2, 2) == 0
   assert check_exact_overlap(s2, s1, 2) == 2
   assert check_exact_overlap(s2, s3, 2) == 2

   res0 = overlaps(data1, lambda s1, s2: check_exact_overlap(s1, s2, 2))
   assert len(res0) == 2, 'You get the wrong number of overlaps'
   assert res0 == {'s0': {'s1': 3, 's3': 2}, 's2': {'s1': 2, 's3': 2}}

   dna_data = read_dna('ex1.fa')
   res1 = overlaps(dna_data, check_exact_overlap)
   assert len(res1) == 5
   for left, right in [('s0', 's1'), ('s1', 's2'), ('s2', 's3'), ('s3', 's4'),
                       ('s4', 's5')]:
       assert res1[left][
           right], f'Missing overlap of {left} and {right} (in that order)'
   print('overlap code passed')
    


def test_all():
    test_class_DnaSeq()
    test_reading()
    test_overlap()
    print('Yay, all good')