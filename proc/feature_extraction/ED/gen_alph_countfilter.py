import numpy as np
import csv
import sys
import json

from basic import *

input_file = '../real_data/AMiner_original_data.txt'
output_file = '../real_data/alph_countfilter_q2.json'

gram_len = 2

data = []
for line in open(input_file):
    #print(line)
    data.append(line[:-1])


data_v = []
for d in data:
    data_v.append(stringToBagofgrams(d, gram_len))

print(data_v[:5])

freqs = {}
count = 0
# stat freq of q-grams
for d in data_v:
    for s in d:
        if s not in freqs:
            freqs[s] = count
            count += 1

print("Alphabet : ", freqs)


# write alph dict
with open(output_file, 'w') as f:
    json.dump(freqs, f)

