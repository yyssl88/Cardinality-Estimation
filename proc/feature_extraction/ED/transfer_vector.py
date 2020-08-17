import numpy as np
import csv
import sys
import json

'''
json_file = '../real_data/alph.json'

input_file = sys.argv[1]
output_file = sys.argv[2]

max_len = 110
'''

json_file = sys.argv[1]
input_file = sys.argv[2]
output_file = sys.argv[3]
max_len = int(sys.argv[4])

data = []
for line in open(input_file):
    #print(line)
    data.append(line[:-1])

# load alphabet
freqs = json.load(open(json_file))

print("Alphabet : ", freqs)

print("max len : ", max_len)

# dimension of vector
dim = len(list(freqs.items())) * max_len

alph_num = len(list(freqs.items()))

print("Dimensionality of Vec : ", dim)

# generate vecs
vec = np.zeros((len(data), dim), dtype=np.uint8)
for rid in range(len(data)):
    d_ = data[rid]
    for sid in range(len(d_)):
        s_ = d_[sid]
        s_c = freqs[s_]
        vec[rid, sid * alph_num + s_c] = 1

np.save(output_file, vec)

