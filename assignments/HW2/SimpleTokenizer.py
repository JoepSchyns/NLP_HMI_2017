import re
import string

class SimpleTokenizer :

    START_TOKEN = "START"
    STOP_TOKEN = "STOP"


    def __init__(self):
        self.scanner = re.Scanner([
          (r"[0-9]+",lambda scanner,token:("INTEGER", token)),
          (r"[a-z_]+",lambda scanner,token:("IDENTIFIER", token)),
         (r"[A-Z_]+", lambda scanner, token: ("IDENTIFIER", token)),
          (r"[,.'\";:<>?]+",lambda scanner,token:("PUNCTUATION", token)),
          (r"\s+", None), # None == skip token.
        ])
        self.tokenizedText = []
        self.remainingText = ""
        self.words = list();


    def tokenize(self,input):
        input = input.lower()

        for c in string.punctuation:
            if (c == '.'):
                input = input.replace(c, " " + self.STOP_TOKEN + " "  + self.START_TOKEN)
            else:
                input = input.replace(c, "")

        result,remainder = self.scanner.scan(input)
        self.tokenizedText = result
        self.remainingText = remainder
        return result

    def readFile(self,path,filename) :
        file = open(path + filename, encoding="utf8")
        text = file.read()
        return text

    def tokenizeFile(self, path, filename) :
        text = self.readFile(path,filename)
        return self.tokenize(text)


    def getWords(self) :
        for token in self.tokenizedText :
            self.words.append(token[1])
        return self.words
