import numpy as np
import csv
import sys
import json
from basic import *

from datasketch import MinHash, MinHashLSHEnsemble

def _minhash(set_, M, k):
    #mask = (1 << b) - 1
    m = MinHash(num_perm=k)
    for e_ in set_:
        m.update(e_.encode('utf8'))
    v_real = np.array(m.digest(), dtype=np.uint64)
    # mask
    v_real = np.bitwise_and(v_real, M)
    return v_real



input_file = sys.argv[1]        # queries: a file storing sets (delimiter = ' ')
output_file = sys.argv[2]       # vectors

b=2
k=256                           # dimensions of vectors


data = []
for line in open(input_file):
    #data.append(line[:-1]) # remove '\n'
    data.append(line)

data_v = []
for d in data:
    data_v.append(d.split())
    #data_v.append(stringToBagofgrams(d, gram_len))

# generate mask
mask = (1 << b) - 1
M = np.array([mask] * k, dtype=np.uint64)

# transfer sets to minhash vectors, each element has b bits
data_minhash = []
for d_s in data_v:
    data_minhash.append(_minhash(d_s, M, k))

data_minhash = np.array(data_minhash, dtype=np.float32)

np.save(output_file, data_minhash)

