import string
import sys
import collections


words = collections.defaultdict(int)
strip = string.whitespace + string.punctuation + string.digits + "\"'"

for filename in sys.argv[1:]:
    for line in open(filename, encoding="utf8"):
        for word in line.lower().split():
            word = word.strip(strip)

            if len(word) > 2:
                words[word] += 1

def order_by_value(key):
    return words[key]

for word in sorted(words, key=order_by_value, reverse=True):
    print(f"'{word}' occurs {words[word]} times")
                