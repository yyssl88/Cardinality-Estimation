import numpy as np
import csv
import sys
import json

json_file = '../real_data/alph.json'

input_file = sys.argv[1]
output_file = sys.argv[2]

max_len = 110

data = []
for line in open(input_file):
    #print(line)
    data.append(line[:-1])

# load alphabet
freqs = json.load(open(json_file))

print("Alphabet : ", freqs)

print("max len : ", max_len)

# dimension of vector
dim = ( len(list(freqs.items())) + 1 ) * max_len

# extra "#"
alph_num = len(list(freqs.items())) + 1

print("Dimensionality of Vec : ", dim)

# generate vecs
vec = np.zeros((len(data), dim), dtype=np.uint8)
for rid in range(len(data)):
    d_ = data[rid]
    for sid in range(len(d_)):
        s_ = d_[sid]
        if s_ == "#":
            s_c = alph_num - 1
        else:
            s_c = freqs[s_]
        vec[rid, sid * alph_num + s_c] = 1

input_file_1 = sys.argv[3]
data_2 = []
for line in open(input_file_1):
    data_2.append(line[:-1])

for rid in range(len(data_2)):
    d_ = data_2[rid]
    for sid in range(len(d_)):
        s_ = d_[sid]
        if s_ == "#":
            s_c = alph_num - 1
        else:
            s_c = freqs[s_]
        vec[rid, sid * alph_num + s_c] = 1

input_file_2 = sys.argv[4]
data_3 = []
for line in open(input_file_2):
    data_3.append(line[:-1])

for rid in range(len(data_3)):
    d_ = data_3[rid]
    for sid in range(len(d_)):
        s_ = d_[sid]
        if s_ == "#":
            s_c = alph_num - 1
        else:
            s_c = freqs[s_]
        vec[rid, sid * alph_num + s_c] = 1

np.save(output_file, vec)

