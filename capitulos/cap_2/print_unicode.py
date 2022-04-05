import sys
import unicodedata

def print_unicode_table(word):
    print(f"decimal   hex   chr   {'name':^40}")
    print(f"-------   ---   ---   {'':-<40}")

    code = ord(' ')
    end = sys.maxunicode

    while code < end:
        c = chr(code)
        name = unicodedata.name(c, "*** unknown ***")
        if word is None or word in name.lower():
            print(f"{code:7}   {code:5x}   {code:^3c}   {name.title()}")
        
        code += 1

word = None
if len(sys.argv[1]) > 1:
    if sys.argv[1] in ("-h", "--help"):
        print(f"usage: {sys.argv[0]} [string]")
        word = 0
    else:
        word = sys.argv[1].lower()

if word != 0:
    print_unicode_table(word)