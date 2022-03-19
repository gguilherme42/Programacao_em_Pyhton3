import string
import sys


words = {}
strip = string.whitespace + string.punctuation + string.digits + "\"'"

for filename in sys.argv[1:]:
    for line in open(filename, encoding="utf8"):
        for word in line.lower().split():
            word = word.strip(strip)

            if len(word) > 2:
                words[word] = words.get(word, 0) + 1

def order_by_value(key):
    return words[key]

for word in sorted(words, key=order_by_value):
    print(f"'{word}' occurs {words[word]} times")
                