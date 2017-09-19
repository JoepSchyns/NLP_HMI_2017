import SimpleTokenizer
class Ngramizer :
    def __init__(self):
        self.ngrams = list()

    def ngramilize(self,words,n) : #TODO stop at the stop token
        ngram = list()
        i = 0
        while i < len(words):
            if not (SimpleTokenizer.SimpleTokenizer.START_TOKEN in words[i + 1 : i + n] or SimpleTokenizer.SimpleTokenizer.STOP_TOKEN in words[i : i + n - 1] ) : #wheiter the start and stop token are not in the middle of the n gram
                ngram.append(" ".join(words[i:(i + n)])) #get ngram and add to the list
            i += n + 1;

        self.ngrams.insert(n,ngram)
        return ngram

    def extend(self,ngramizer):
        for i in range(0,len(ngramizer.ngrams)) :
            if len(self.ngrams) - 1 < i : #if the ngram does not have the current n
                self.ngrams.insert(i,ngramizer.ngrams[i])
            else:
                self.ngrams[i].extend(ngramizer.ngrams[i])

        return self.ngrams
