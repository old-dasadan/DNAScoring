from os import path

import seqfold

from seqfold.fold import dg, fold

import pandas as pd

import numpy as np

print(seqfold.__file__)

DIR = path.dirname(path.realpath(__file__))

#read random DNA seq file
for index in range(100, 200):
    data=[]
    with open(path.join(DIR, "rand_dna_seq_100-200nt", "rand_dna_seq_" + str(index) + ".csv"), 'r',encoding='utf-8-sig') as f_input:
        for line in f_input:
            data.append(list(line.strip().split(',')))
    dataset=pd.DataFrame(data)

    DNA_EXAMPLES = []

    len_row = dataset.shape[0]
    for i in range(0, 1000):
        #retrieve each DNA seq in string form
        df_i = dataset[i:i+1].dropna(axis = 1)
        array_i_np = np.array(df_i)
        len_i = df_i.shape[1]
        row_i = ''
        for j in range(0, len_i):
            str_j = str(array_i_np[0, j])
            row_i += str_j
        DNA_EXAMPLES.append(row_i)


    # DNA_EXAMPLES = {
    #     "GGGAGGTCGTTACATCTGGGTAACACCGGTACTGATCCGGTGACCTCCC": -10.9,  # three branched structure
    #     "GGGAGGTCGCTCCAGCTGGGAGGAGCGTTGGGGGTATATACCCCCAACACCGGTACTGATCCGGTGACCTCCC": -23.4,  # four branched structure
    #     "CGCAGGGAUACCCGCG": -3.8,
    #     "TAGCTCAGCTGGGAGAGCGCCTGCTTTGCACGCAGGAGGT": -6.9,
    #     "GGGGGCATAGCTCAGCTGGGAGAGCGCCTGCTTTGCACGCAGGAGGTCTGCGGTTCGATCCCGCGCGCTCCCACCA": -15.5,
    #     "TGAGACGGAAGGGGATGATTGTCCCCTTCCGTCTCA": -18.1,
    #     "ACCCCCTCCTTCCTTGGATCAAGGGGCTCAA": -3.7,
    #     "TGTCAGAAGTTTCCAAATGGCCAGCAATCAACCCATTCCATTGGGGATACAATGGTACAGTTTCGCATATTGTCGGTGAAAATGGTTCCATTAAACTCC": -9.4,
    # }

    # writing results to examples for comparison
    DNA_RESULTS = {}

    for seq in DNA_EXAMPLES:
        ss = fold(seq, temp=75.0)
        cdg = round(sum(s.e for s in ss), 2)

        descs = []
        ijs = []
        for s in ss:
            descs.append(s.desc)
            ijs.append(s.ij)
        descs_str = ''.join(descs)
        ijs_str = ''.join('%s' %id for id in ijs)

        #score of each seq
        score = round(2 * len(ijs) / len(seq), 2)

        DNA_RESULTS[seq] = (score, cdg, descs_str, ijs_str)

    # save DNA_RESULTS to examples
    with open(path.join(DIR, "..", "examples","rand_dna_seq_result_" + str(index) + ".csv"), "w") as ex:
        ex.write("score,seqfold,description,inward children,seq\n")

        for seq, (sc, sf, df, ijf) in DNA_RESULTS.items():
            ex.write(",".join([str(sc), str(sf), df, ijf, seq]) + "\n")