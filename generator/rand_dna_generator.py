import numpy as np
import csv
import random
import matplotlib.pyplot as plt
from os import path
import seqfold

DNA_base = ['A', 'G', 'C', 'T']

DNA_Sequence = []

DIR = path.dirname(path.realpath(__file__))

for i in range(50, 150):
    
    with open(path.join(DIR, 'rand_dna_seq_' + str(i) + '.csv'), 'w', newline = '') as file_output:
    
        n = 0
        while n < 1000:
            seq = ""
            GC_num = 0
            seq_len = i
            j = 0
            while j < seq_len:
                Nth = random.randint(0,3)
                if Nth == 1 or Nth == 2:
                    GC_num += 1
                seq += DNA_base[Nth]
                j += 1
                #限制多聚物
                if len(seq) > 4 and len(set(seq[-4:])) == 1:
                    seq = seq[:-1]
                    j -= 1

            #限制GC含量45%-55%
            if float(GC_num/seq_len) >= 0.45 and float(GC_num/seq_len) <= 0.55:
                file_output.write(seq + "\n")
                n += 1
                DNA_Sequence.append(seq)
