import re
import string

class SimpleTokenizer :
    def __init__(self):
        self.scanner = re.Scanner([
          (r"[0-9]+",lambda scanner,token:("INTEGER", token)),
          (r"[a-z_]+",lambda scanner,token:("IDENTIFIER", token)),
          (r"[,.'\";:<>?]+",lambda scanner,token:("PUNCTUATION", token)),
          (r"\s+", None), # None == skip token.
        ])


    def tokenize(self,str):
        str = str.lower()

        for c in string.punctuation:
            str = str.replace(c, "")

        return self.scanner.scan(str);

