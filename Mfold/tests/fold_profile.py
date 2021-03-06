import profile
import pstats

from seqfold import dg

# ~taking ~21 seconds from CLI, too slow with profiler
# ~16.5 seconds with Cython
STATS_FILE = "fold_profile.stats"

SEQ = "'GAAATAGACGCCAAGTTCAATCCGTACTCCGACGTACGATGGAACAGTGTGGATGTGACGAGCTTCATTTATACCCTTCGCGCGCCGGACCGGGGTCCGCAAGGCGCGGCGGTGCACAAGCAATTGACAACTAACCACCGTGTATTCGTTATGGCACCAGGGAGTTTAAGCCGAGTCAATGGAGCTCGCAATACAGAGTT'"
SCRIPT = f"dg({SEQ}, 37.0)"
print(SCRIPT)
profile.run(SCRIPT, STATS_FILE)

STATS = pstats.Stats(STATS_FILE)
STATS.strip_dirs()
STATS.sort_stats("cumulative")
STATS.print_stats()

