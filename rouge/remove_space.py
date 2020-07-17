# -*- coding: utf-8 -*-
import os
import multiprocessing
import timeit

# get file content
def get(file):
    current_path=os.path.dirname(os.path.abspath(__file__))
    data_path=os.path.join(current_path,'data')
    print(data_path)
    data=os.path.join(data_path,file+'.txt')
    
    with open(data,'r',encoding='utf-8') as f:
        content=f.readlines()
        
    return content

def out(file):
    content = get(file)
    current_path = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_path,'data')
    out_path = os.path.join(data_path, file + '_nospace.txt')


    with open(out_path, 'w', encoding='utf-8') as output:
        for sentence in content:
            output.write(sentence.replace(" ",""))

if __name__=='__main__':
    start=timeit.default_timer()
    
    print(out('pred_20191107'))
    end=timeit.default_timer()
    print('%.2f secs used.'%(end-start))