# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import nltk
import re
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.feature_extraction.text import TfidfTransformer  

sentences=[]

def cut_sent(para):
    para = re.sub('([。！？\?])([^”’])', r"\1\n\2", para)  # 单字符断句符
    para = re.sub('(\.{6})([^”’])', r"\1\n\2", para)  # 英文省略号
    para = re.sub('(\…{2})([^”’])', r"\1\n\2", para)  # 中文省略号
    para = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)
    # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
    para = para.rstrip()  # 段尾如果有多余的\n就去掉它
    # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
    return para.split("\n")


import numpy as np

    
def wordsummary(sentences):
        #sentences = text.split("。")#将文本切分为句子。
        new_sentences = []
        sentence_score = {}
        words_in_sentences = []
        word_weight = {}#存储本文档中各个词语的term freq
        #print("计算次词语权重")
        for sentence in sentences:
            
            sentence=sentence.replace("？","")
            sentence=sentence.replace("！","")
            sentence=sentence.replace("#","")
            sentence=sentence.replace("。","")
            sentence=sentence.replace("，","")
            sentence=sentence.replace("“","")
            sentence=sentence.replace("”","")
            sentence=sentence.replace("；","")
            sentence=sentence.replace("《","")
            sentence=sentence.replace("》","")
            sentence=sentence.replace("、","")
            sentence=sentence.replace("：","")
            sentence=sentence.replace("\"","")
            sentence=sentence.replace("（","")
            sentence=sentence.replace("）","")
            sentence=sentence.replace(".","")
            sentence=sentence.replace("…","")
            sentence=sentence.replace("-","")
            sentence=sentence.replace("=","")
            sentence=sentence.replace(")","")
            sentence=sentence.replace("(","")
            sentence=sentence.replace("↓","")
            sentence=sentence.replace("→","")
            sentence=sentence.replace(">","")
            sentence=sentence.replace("<","")
            sentence=sentence.replace(":","")
            sentence=sentence.replace(";","")
            sentence=sentence.replace("_","")
            sentence=sentence.replace("!","")
            sentence=sentence.replace("?","")
            sentence=sentence.replace("/","")
            sentence=sentence.replace("【","")
            sentence=sentence.replace("】","")
            sentence=sentence.replace("+","")
            sentence=sentence.replace("·","")
            sentence=sentence.replace("—","")
            sentence=sentence.replace("×","")
            sentence=sentence.replace("~","")
            sentence=sentence.replace("～","")
            words = sentence.split(' ')#对句子分词，得到词语list
            for word in words:
                word_weight[word] = word_weight.get(word, 0) + 1
            words_in_sentences.append(words)
            new_sentences.append(sentence)
        #print("计算word权重", word_weight)

        for i in range(len(new_sentences)):
            sentence_score[new_sentences[i]] = np.sum([word_weight[word] for word in words_in_sentences[i]])

        #print("get top score text")
        word_sorted = sorted(word_weight.items(), key=lambda x: x[1], reverse=True)[:11]
        #print(word_sorted)
        word_summary=" ".join(map(lambda x: x[0],word_sorted))
        print('word_summary:',word_summary)

       # print('summary : ',summary)
        return word_summary

def sensummary(sentences):
        #sentences = text.split("。")#将文本切分为句子。
        new_sentences = []
        sentence_score = {}
        words_in_sentences = []
        word_weight = {}#存储本文档中各个词语的term freq
        #print("计算次词语权重")
        for sentence in sentences:
            words = sentence.split(' ')#对句子分词，得到词语list
            for word in words:
                word_weight[word] = word_weight.get(word, 0) + 1
            words_in_sentences.append(words)
            new_sentences.append(sentence)

        for i in range(len(new_sentences)):
            sentence_score[new_sentences[i]] = np.sum([word_weight[word] for word in words_in_sentences[i]])

        sentence_sorted = sorted(sentence_score.items(), key=lambda x: x[1], reverse=True)[:3]
        sentence_summary = "".join(map(lambda x: x[0], sentence_sorted))
        print('sentence_summary:',sentence_summary)

       # print('summary : ',summary)
        return sentence_summary  
    
        
    
    
def tfidf(docname):
    f=open(docname,'r') 
    lines=f.readlines()
    f.close()
    #类调用  
    Tfidftransformer = TfidfTransformer()  
    f = open('test_longtextsummary_10.txt','w')
    f2 = open('test_longsensummary_2.txt','w')
    for i in range(len(lines)):
        #print("orginal sentences"+lines[i])
        sentences=cut_sent(lines[i])
        #print('cut sentence'+str(sentences))
        #print('sentences lengh'+str(len(sentences)))
        vectorizer = CountVectorizer(min_df=1, max_df=1.0, token_pattern='\\b\\w+\\b')
        #计算个词语出现的次数  
        X = vectorizer.fit_transform(sentences)  
        #获取词袋中所有文本关键词   
        word = vectorizer.get_feature_names()  
        #print(word)  
        #查看词频结果  
        #print(X.toarray())
        
        #print(Tfidftransformer)  
        #将词频矩阵X统计成TF-IDF值  
        tfidf = Tfidftransformer.fit_transform(X)  
        #查看数据结构 tfidf[i][j]表示i类文本中的tf-idf权重  
        #print(tfidf.toarray())       
        temp=wordsummary(sentences)
        temp2=sensummary(sentences)
        f.write(temp+'\n')
        f2.write(temp2+'\n')
    f.close()
    f2.close()

if __name__ == '__main__':
     #tfidf('/home/miko/myexp/data/word/src-train_word.txt')
     tfidf('/home/miko/myexp/測試.txt')



