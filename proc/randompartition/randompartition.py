import numpy as np
import os
import sys

original_data_file = sys.argv[1]
part_num = int(sys.argv[2])
save_file_prefix = sys.argv[3]

#original_data_file = '/import/sigmod05/1/scratch/yaoshuw/SphericalRangeCardEstimation/data/fasttext/real_data/fasttext_wiki_d300_1M.npy'

fasttext_originalData = np.load(original_data_file)

print('Shape : ', fasttext_originalData)

# random shuffle
#part_num = int(sys.argv[1])

data_num = fasttext_originalData.shape[0]

part_size = data_num // part_num

np.random.seed(20)
np.random.shuffle(fasttext_originalData)


random_partition_vecs = []
for pid in range(part_num - 1):
    start_id = pid * part_size
    end_id = (pid + 1) * part_size
    random_partition_vecs.append(fasttext_originalData[start_id : end_id])

random_partition_vecs.append(fasttext_originalData[(part_num - 1) * part_size : ])

#save_file_prefix = './fasttext_random_partitions_partNum' + str(part_num) + '/fasttext_wiki_d300_randomPartition_part'
# write file
for pid in range(part_num):
    save_file = save_file_prefix + str(pid) + '.npy'
    print(random_partition_vecs[pid].shape)
    np.save(save_file, random_partition_vecs[pid])



