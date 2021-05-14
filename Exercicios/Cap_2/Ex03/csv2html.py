import sys


def print_start():
    print('<table border="1" >')


def print_line(line, color, max_width):
    print(f'<tr bgcolor={color}>')
    fields = extract_fields()

    for field in fields:
        if not field:
            print('<td></td>')
        else:
            number = field.replace(",", "")
            try:
                float_number = float(number)
                print(f'<td align="right">{round(float_number):d}</td>')
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                field = escape_html(field)

                if len(field) <= max_width:
                    print(f'<td>{field}</td>')
                else:
                    print(f'<td>{field:.{max_width}}...</td>')
                print('</tr>')


def extract_fields(line):
    fields = []
    field = ""
    quote = None
    for character in line:
        if character in "\"'":
            if quote is None: # começo da string com aspas
                quote = character
            elif quote == character: # fim da string com aspas
                quote = None
            else:
                field += character # outra aspa dentro de uma string com aspas
            continue
        if quote is None and character== ",": # fim de um campo
            fields.append(field)
            field = ""
        else:
            field += character # Acumulando um campo
        if field:
            fields.append(field) # adicionando o último campo

        return fields


def escape_html(text):
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    return text


def print_end():
    print('</table>')


def main():
    max_width = 100 # limita o número de caracteres numa célula
    count = 0
    print_start()
    color = "lightyellow"
    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            else:
                color = "lightyellow"

                print_line(line, color, max_width)
                count += 1
        except EOFError:
            break

    print_end()


main()
