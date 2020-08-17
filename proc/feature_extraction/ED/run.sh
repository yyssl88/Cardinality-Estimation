#!/bin/bash

DATA=$1   	# the original dataset, e.g., AMiner
alph=$2   	# the alphabet set file
maxlen=$3 	# the maximum length of strings
queries=$4 	# training, validation, testing instances (or features)
vecs=$5		# output vectors of ${queries}

# generate alphabet set
python gen_alph.py ${DATA} ${alph} ${maxlen}

# transform strings to vectors
python transfer_vector.py ${alph} ${queries} ${vecs} ${maxlen} 
