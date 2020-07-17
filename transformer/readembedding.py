# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def read_embeddings(file_enc, skip_lines=0, filter_set=None):
    embs = dict()
    total_vectors_in_file = 0
    with open(file_enc, 'rb') as f:
        for i, line in enumerate(f):
            if i < skip_lines:
                continue
            if not line:
                break
            if len(line) == 0:
                # is this reachable?
                continue

            l_split = line.decode().strip().split(' ')
            if len(l_split) == 2:
                continue
            total_vectors_in_file += 1
            if filter_set is not None and l_split[0] not in filter_set:
                continue
            embs[l_split[0]] = [float(em) for em in l_split[1:]]
    return embs, total_vectors_in_file

if __name__=="__main__":
        embs, total_vectors_in_file=read_embeddings('data/small/data.valid.02.pt')