import jieba                                           #导入jieba模块
import re 
import jieba.posseg as pseg 
import jieba.analyse
from os import path
import os
from pymongo import MongoClient

def get_data_from_db(outputFile):
    jobCollection=MongoClient('mongodb://localhost:27017/').Job.Lagou
    content=''
    for item in jobCollection.find({ "Flag" : True},{'Details':1}):
        if item["Details"]:
            content+=item["Details"]
    fout = open(outputFile, 'w', encoding='UTF-8')   
    fout.write(content)  

def remove_stopwords(text):
    jieba.analyse.set_stop_words('C:\\Users\\Kevin\\Desktop\\PythonProject\\DataVisualization\\stop_words.txt')
    tags = jieba.analyse.extract_tags(text,200)
    return tags

def splitSentence(outputFile):
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    jieba.load_userdict(path.join(d,'DataVisualization','newdict.txt'))
    jobCollection=MongoClient('mongodb://localhost:27017/').Job.Lagou
    content=''
    for item in jobCollection.find({ "Flag" : True},{'Details':1}):
        if item["Details"]:
            content+=item["Details"]
    jb=jieba.lcut(content)     
    result = remove_stopwords(' '.join(jb))
    print(result)
    fout = open(outputFile, 'w', encoding='UTF-8') 
    fout.write(' '.join(result))       #将分词好的结果写入到输出文件
    fout.close()  

#创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath,'r',encoding='utf-8').readlines()]
    return stopwords

def splitSentence_old(inputFile, outputFile):

    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    jieba.load_userdict(path.join(d,'DataVisualization','newdict.txt'))                     
    #把停用词做成字典
    stopwords = {}
    fstop = open(path.join(d, 'DataVisualization','stop_words.txt'),'r', encoding='UTF-8')
    for eachWord in fstop:
        stopwords[eachWord.strip()] = eachWord.strip()
    fstop.close()

    fin = open(inputFile, 'r', encoding='UTF-8')    
    fout = open(outputFile, 'w', encoding='UTF-8')                                #以写得方式打开文件  
    for eachLine in fin:
        line = eachLine.strip()       #去除每行首尾可能出现的空格，并转为Unicode进行处理 

        wordList = list(jieba.cut(line)) #用结巴分词，对每行内容进行分词  
        outStr = ''  
        for word in wordList:
            if word not in stopwords:  
                outStr += word  
                outStr += ' '  
        fout.write(outStr.strip() + '\n')       #将分词好的结果写入到输出文件
    fin.close()  
    fout.close()  


if __name__ == '__main__':
    d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()
    # jobtxt=path.join(d,'job.txt')
    # get_data_from_db(jobtxt)
    splitSentence( path.join(d,'result.txt'))
    # splitSentence(jobtxt, path.join(d,'result.txt'))