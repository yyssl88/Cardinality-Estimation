import numpy as np
import csv
import sys
import json
from basic import *


json_file = '../real_data/alph_countfilter_q2.json'

input_file = sys.argv[1]
output_file = sys.argv[2]

gram_len = int(sys.argv[3])

data = []
for line in open(input_file):
    data.append(line[:-1])

data_v = []
for d in data:
    data_v.append(stringToBagofgrams(d, gram_len))

# load alphabet
freqs = json.load(open(json_file))

# dimension of vector
dim = len(list(freqs.items()))

print("Dimensionality of Vec : ", dim)

# generate vecs
vec = np.zeros((len(data), dim), dtype=np.uint8)
for rid in range(len(data_v)):
    d_ = data_v[rid]
    for sid in range(len(d_)):
        s_ = d_[sid]
        s_c = freqs[s_]
        vec[rid, s_c] = 1

np.save(output_file, vec)

