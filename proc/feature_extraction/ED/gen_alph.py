import numpy as np
import csv
import sys
import json

'''
input_file = '../real_data/AMiner_original_data.txt'
output_file = '../real_data/alph.json'

max_len = 50
'''

input_file = sys.argv[1]
output_file = sys.argv[2]
max_len = int(sys.argv[3])

data = []
for line in open(input_file):
    #print(line)
    data.append(line[:-1])


freqs = {}
count = 0
# stat freq of 1-grams
for d in data:
    for s in d:
        if s not in freqs:
            freqs[s] = count
            count += 1

print("Alphabet : ", freqs)


# write alph dict
with open(output_file, 'w') as f:
    json.dump(freqs, f)


'''
max_len = min(maxlen, max_len)
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
'''
