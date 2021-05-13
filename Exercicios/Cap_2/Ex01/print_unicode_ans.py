import sys
import unicodedata


def print_unicode_table(word_list_input):

    for word in word_list_input:
        print(f'\n>>>>>>>>> {word}')
        print(f'decimal  hex  chr  {"name": ^40}')
        print(f'-------  ---  ---  {"":-<40}')

        code = ord(" ")  # first unicode character
        end = sys.maxunicode  # last unicode character

        while code < end:
            character = chr(code)
            name = unicodedata.name(character, '*** unknown ***')

            if word is None or word in name.lower():
                print(f'{code:7} {code:5X} {code:^3c} {name.title()}')
                    # decimal inteiro - hexadecimal maiúsculo - caractere
            code += 1


if len(sys.argv) > 1:
    if sys.argv[1] in ('-h', '--help'):
        print(f'usage: {sys.argv[0]} [string]')
    else:
        word_list = [word.lower() for word in sys.argv[1:]]
        print_unicode_table(word_list)