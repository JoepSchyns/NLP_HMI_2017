import re

import math

from assignments.HW2 import SimpleTokenizer
from collections import defaultdict



class Ngramizer :

    CORPUS_FILE = "../../datasets/blogs/ngramCorpus.txt"
    MINIMUM_FREQ = 24

    def __init__(self):
        self.ngrams = list()
        self.ngramsFrequencies = list()
        self.vSize = list();

    def ngramilize(self,words,n) :
        ngram = list()
        i = 0
        while i < len(words):
            if not (SimpleTokenizer.SimpleTokenizer.START_TOKEN in words[i + 1 : i + n] or SimpleTokenizer.SimpleTokenizer.STOP_TOKEN in words[i : i + n - 1] ) : #wheiter the start and stop token are not in the middle of the n gram
                ngram.append(" ".join(words[i:(i + n)])) #get ngram and add to the list
            i += 1;

        self.ngrams.insert(n,ngram)
        return ngram

    def extend(self,ngramizer):
        for i in range(0,len(ngramizer.ngrams)) :
            if len(self.ngrams) - 1 < i : #if the ngram does not have the current n
                self.ngrams.insert(i,ngramizer.ngrams[i])
            else:
                self.ngrams[i].extend(ngramizer.ngrams[i])

        return self.ngrams

    def frequencies(self,list):

        frequencyList = defaultdict(int)
        for item in list:
            frequencyList[item] += 1

        return frequencyList

    def calcFrequencies(self):
        for ngram in self.ngrams:
            frequencyList = self.frequencies(ngram);
            frequencyList = sorted(frequencyList.items(), key=lambda x: x[1], reverse=True)
            self.ngramsFrequencies.append(frequencyList)

        return self.ngramsFrequencies

    def readCorpus(self,indentifierName,n):
        for i in range(0,n) :
            self.vSize.insert(i,0)
            ngramFrequencies = list()
            file = open(self.CORPUS_FILE + indentifierName + str(i), encoding="utf8")
            text = file.read()
            lines = text.split('\n')
            for line in lines:
                line = re.sub('[)(\']',"",line)
                split = line.split(",")
                if len(split) == 2 :
                    ar = [None] * 2
                    ar[0] = split[0]
                    ar[1] = int(split[1])
                    self.vSize[i] += ar[1]
                    ngramFrequencies.append(ar)

            self.ngramsFrequencies.insert(n,ngramFrequencies);

    def createCorpusFile(self,indentifierName):
        n = 0
        for ngramFrequencies in self.ngramsFrequencies:
            file = open(self.CORPUS_FILE + indentifierName + str(n), 'w+')
            for word in ngramFrequencies:
                if word[1] > MINIMUM_FREQ :
                    file.write("%s\n" % str(word))

            n += 1

    K = 0.13



    def probability(self,freq,K,N,V):
        return (freq + K) / (N+ K * V)

    def calculateTotalProb(self,tokensFile,n):
        totalProb = 0;
        for token in tokensFile:
            prob = self.findProb(token,len(tokensFile),n)
            #print(str(token) + " " + str(prob))
            totalProb += math.log2(prob)
        return totalProb

    def findProb(self,token,amountTokens,n):
        ngramFrequencies = self.ngramsFrequencies[n]

        for tokenFrequency in ngramFrequencies:
            if token == tokenFrequency[0] and tokenFrequency[1] > self.MINIMUM_FREQ: #only use words occurentes that are 25 or higher
                return self.probability(tokenFrequency[1],self.K,self.vSize[n],amountTokens)

        return self.probability(0,self.K,self.vSize[n],amountTokens)

