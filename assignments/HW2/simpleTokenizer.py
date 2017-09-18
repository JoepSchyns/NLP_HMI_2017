import re
scanner=re.Scanner([
  (r"[0-9]+",lambda scanner,token:("INTEGER", token)),
  (r"[a-z_]+",lambda scanner,token:("IDENTIFIER", token)),
  (r"[,.'\";:<>?]+",lambda scanner,token:("PUNCTUATION", token)),
  (r"\s+", None), # None == skip token.
])

sentences = ["I'm feeling a bit low these days, obviously because of the gargantuan amount of work that I do.",
             "You can hear them run when you turn on the lights, their hairy legs brushing against the darkness, stealthily.",
             "Restaurants proudly display a letter grade of 'A' on their windows, a grade lower and even baser than the scarlet letter, because it is bought not earned."];

for sentence in sentences :
    sentence = sentence.lower()
    results, remainder = scanner.scan(sentence);
    print("results:")
    print(results)
    print("remainder:")
    print(remainder)
