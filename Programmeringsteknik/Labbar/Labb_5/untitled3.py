
# -*- coding: utf-8 -*-

#DA2004 HT21
# Laboration 5 - Överlappande DNA

class DnaSeq:
    def __init__(self, accession, seq):
        """DNA sequence class initialisation. Parameters may not be empty strings or Null."""
        if not accession or not seq:
            raise ValueError
        assert len(accession) != 0 or len(seq) != 0
        self.accession = accession
        self.seq = seq

    def __len__(self):
        """ Överlagring av "len" funktioner. Returernar DNA sekvensens längd."""
        dna_sequence_length = len(self.seq)
        return dna_sequence_length

    def __str__(self):
        """Överlagring av "str" funktioner. Returernar 
        utskriftsbar (sträng) version av DNA informationen, dvs dess accession."""
        text = "<DnaSeq accession={}>".format(self.accession)
        return text


def check_valid_dna_sequence(dna_sequence):
    """ Verify the DNA sequence string is a valid. Characters for a valid DNA sequence is declared locally. """
    if not dna_sequence:
        return False
    valid_dna_sequence_elements = ['A', 'C', 'G', 'T']
    dna_sequence_is_valid = all([element in valid_dna_sequence_elements for element in dna_sequence])
    return dna_sequence_is_valid;


def read_dna(filename):
    """Read DNA declarations from formatted text file. Return a list of DnaSeq instances.
    
    Fileformat for text file:
        >accession
        dna_sequence"""
    dnaSeq_list = []  # list of DnaSeq to return
    dna_accession_precursor = '>'
    file_mode = 'r'

    with open(filename, file_mode) as filehandle:
        dna_sequence_from_file = True
        # get frist dna accession from tile
        dna_accession_from_file = filehandle.readline()
        while dna_accession_from_file and dna_sequence_from_file:
            # if not the dna asseccion precursor is found first in line
            # then read next line with out processing 
            if dna_accession_from_file[0] == dna_accession_precursor:
                # strip precursor from start of line
                # strip end of line and blank space characters from end, beginning of line
                dna_accession_from_file = dna_accession_from_file.lstrip(dna_accession_precursor).strip()
                dna_accession_from_file = dna_accession_from_file.strip()

                # read asseccion and dna sequence
                # strip line ending, blank space from end, beginning of line
                # dna sequence needs to contain only valid elements
                dna_sequence_from_file = filehandle.readline().strip()
                dna_sequence_from_file = dna_sequence_from_file.strip()
                if check_valid_dna_sequence(dna_sequence_from_file):
                    dna_obj = DnaSeq(dna_accession_from_file, dna_sequence_from_file)
                    dnaSeq_list.append(dna_obj)
            # get next dna accession from file 
            dna_accession_from_file = filehandle.readline()

    return dnaSeq_list



def check_exact_overlap(sequence_obj_a, sequence_obj_b, min_length = 10):
    """ Compare sequence a from the right and sequence b from the left. 
    Return 0 if no overlap or if overlap is not longer then minimal required length."""
    length_overlap = 0
    sequence_a = sequence_obj_a.seq
    sequence_b = sequence_obj_b.seq
    len_a = len(sequence_a)
    len_b = len(sequence_b)
    max_overlap = min(len_a, len_b) # max possible overlap is the shortest string

    # if minimal required length overlap is longer then possible overlap    
    if (max_overlap < min_length):
        return length_overlap
    
    # check longest possible overlap and then shorter
    # substring from sequence_a is taken from the end/right part of the string
    # substring from sequence_a is taken from the starting/left part of the string    
    for index in range(max_overlap):
        position_start_a = len_a - max_overlap + index
        position_end_a = len_a
        position_start_b = 0
        position_end_b = max_overlap -index
        string_a = sequence_a[position_start_a:position_end_a]
        string_b = sequence_b[position_start_b:position_end_b]
        if (string_a == string_b):
            length_overlap =  max_overlap-index 
            break   # longest overlap is accepted
    
    # Check so overlap is longer then minimum required, else it does not count
    if (length_overlap < min_length):
        length_overlap = 0

    return length_overlap



def overlaps(dnaSeq_list, f):
    """ All detectable overlaps among pairs of sequences in the input list are to be returned."""
    result_dict = {}
    seq_list_length = len(dnaSeq_list)
    if (not seq_list_length): print('empty dna list')
    for i in range(seq_list_length):
        for j in range(seq_list_length):
            if (i != j ):
                dna_object_1 = dnaSeq_list[i]
                dna_object_2 = dnaSeq_list[j]
                accession1 = dna_object_1.accession
                accession2 = dna_object_2.accession

                # call paramter function to compare two dna sequence
                result_length = f(dna_object_1, dna_object_2)
                if (result_length):
                    result_dict[accession1]= {accession2:result_length}
    return result_dict


#
# Testing code. You should not change any line after this one!
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