import os

import multiprocessing
import timeit


def get(file):
    current_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_path, 'data')
    data = os.path.join(data_path, file+'.txt')

    with open(data, 'r', encoding='utf-8') as f:
        content = f.readlines()

    return content

def cut(string):
    return [i for i in string]


def mulit(file):
    pool = multiprocessing.Pool(processes=16)
    strings = pool.map(cut, get(file))

    return strings

def out(file):
    data = mulit(file)
    current_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_path, 'data')
    out_path = os.path.join(data_path, file + '_space.txt')


    with open(out_path, 'w', encoding='utf-8') as o:
        for line in data:
            o.write(' '.join(line))


if __name__ == '__main__':
    start = timeit.default_timer()

    out('')


    end = timeit.default_timer()
    print('%.2f secs used.'%(end-start))

'''
get('tgt-test.txt', 1000)
get('tgt-train.txt', 10000)
get('tgt-val.txt', 500)
get('src-test.txt', 1000)
get('src-train.txt', 10000)
get('src-val.txt', 500)
'''