from os import path

from seqfold.fold import dg, fold

import seqfold

print(seqfold.__file__)

DIR = path.dirname(path.realpath(__file__))

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

# # writing results to examples for comparison
# DNA_RESULTS = {}

# for seq, ufold in DNA_EXAMPLES.items():
#     ss = fold(seq, temp=37.0)
#     cdg = round(sum(s.e for s in ss), 2)
#     DNA_RESULTS[seq] = (cdg, ufold)

# # save DNA_RESULTS to examples
# with open(path.join(DIR, "..", "examples", "dna.csv"), "w") as ex:
#     ex.write("seqfold,UNAFold,seq\n")

#     for seq, (sf, uf) in DNA_RESULTS.items():
#         ex.write(",".join([str(sf), str(uf), seq]) + "\n")


RNA_EXAMPLES = [
    'GGAUACGGCCAUACUGCGCAGAAAGCACCGCUUCCCAUCCGAACAGCGAAGUUAAGCUGCGCCAGGCGGUGUUAGUACUGGGGUGGGCGACCACCCGGGAAUCCACCGUGCCGUAUCCU',
    'GGACCUGGUGGCUAUGGCGGGAGAGAUCCACCCGAUCCCAUCCCGAACUCGGCCGUGAAAACCCCCAGCGCCUAUGAUACUGCGGCUUAAGCCGUGGGAAAGUCGGUCGCCGCCAGGUCC',
]


# writing results to examples for comparison
RNA_RESULTS = {}

for seq in RNA_EXAMPLES:
    ss = fold(seq, temp=37.0)
    cdg = round(sum(s.e for s in ss), 2)

    descs = []
    ijs = []
    for s in ss:
        descs.append(s.desc)
        ijs.append(s.ij)
    descs_str = ''.join(descs)
    ijs_str = ''.join('%s' %id for id in ijs)

    RNA_RESULTS[seq] = (cdg, descs_str, ijs_str)

# save RNA_RESULTS to examples
with open(path.join(DIR, "..", "examples", "rna.csv"), "w") as ex:
    ex.write("seqfold,description,inward children,seq\n")

    for seq, (sf, df, ijf) in RNA_RESULTS.items():
        ex.write(",".join([str(sf), df, ijf, seq]) + "\n")

