def program_usage():
    print("Usage:")
    print("csv2.html.py [maxwidth=int] [format=str] < infile.csv > outfile.html")
    print()
    print("maxwdith é um integer opcional; se especificado, configura o número máximo de caracteres que podem entrar no campo da string, do contrário, o padrão de 100 caracteres é usado.")
    print()
    print("format é a formatação usada para números; se não especificado o padrão é '.0f'")


def process_options() -> tuple[int, str]:
    import sys

    DEFAULT_MAX_WIDTH = 100
    DEFAULT_FORMAT = ".0f"

    def has_parameters() -> bool:
        return 4 > len(sys.argv) > 1
    
    def has_no_parameters() -> bool:
        return len(sys.argv) == 1
    

    def has_maxwidth(input: str) -> bool:
        return "maxwidth=" in input
    
    def has_format(input: str) -> bool:
        return "format=" in input
    
    def has_maxwidth_and_format() -> bool:
        has_maximum_len = len(sys.argv) == 3

        if has_maximum_len:
            return (has_maxwidth(sys.argv[1]) and has_format(sys.argv[2])) \
                    or \
                    (has_maxwidth(sys.argv[2]) and has_format(sys.argv[1]))

        return  False


    def get_maxwidth(parameter: str) -> int:
        index = parameter.find("=")
        return  int(parameter[index + 1:])
    
    def get_format(parameter: str) -> str:
        index = parameter.find("=")
        return  parameter[index + 1:]

        
    def get_maxwidth_and_format(input_a: str, input_b: str) -> tuple[int, str]:
        width_result = format_result = None

        try:
            width_result = get_maxwidth(input_a)      # sys.argv[1]
            format_result = get_format(input_b)       # sys.argv[2]

        except ValueError:
            try:
                format_result = get_format(input_a)   # sys.argv[1]
                width_result = get_maxwidth(input_b)  # sys.argv[1]
            
            except ValueError:
                return (DEFAULT_MAX_WIDTH, DEFAULT_FORMAT)
 

        return (width_result, format_result)

    def get_parameters() -> tuple:
        if has_maxwidth(sys.argv[1]):
                return (get_maxwidth(sys.argv[1]), DEFAULT_FORMAT)
        elif has_format(sys.argv[1]):
            return (DEFAULT_MAX_WIDTH, get_format(sys.argv[1]))
        else: 
            return (None, None)

    if has_parameters():   
        if sys.argv[1] in ["-h", "--help"]:
            program_usage()
            return (None, None)
        
        if has_maxwidth_and_format():
            return get_maxwidth_and_format(sys.argv[1], sys.argv[2])
        else:
            return get_parameters()

    elif has_no_parameters():
        return DEFAULT_MAX_WIDTH, DEFAULT_FORMAT
    else:
        return (None, None)
    
 
    



def print_start():
    print('<table border="1" >')


def print_line(line: str, color: str, max_width: int, user_format: str):
    print(f'<tr bgcolor="{color}">')
    fields = extract_fields(line)

    for field in fields:
        if not field:
            print('<td></td>')
        else:
            number = field.replace(",", "")
            try:
                float_number = float(number)
                print(f'<td align="right">{round(float_number):user_format}</td>')
            except ValueError:
                field = field.title()
                field = field.replace(" And ", " and ")
                field = escape_html(field)

                if len(field) <= max_width:
                    print(f'<td>{field}</td>')
                else:
                    print(f'<td>{field:.{max_width}}...</td>')
    print('</tr>')


def extract_fields(line: str):
    fields = []
    field = ""
    quote = None
    
    for character in line:
        if character in "\"\'":
            if quote is None: # começo da string com aspas
                quote = character
            elif quote == character: # fim da string com aspas
                quote = None
            
            continue    
        
        if quote is None and character == ",": # fim de um campo
            fields.append(field)
            field = ""
        else:
            field += character # Acumulando um campo

    return fields


def escape_html(text):
    import xml.sax.saxutils

    return xml.sax.saxutils.escape(text)


def print_end():
    print('</table>')


def main():
    max_width, format = process_options() 
    if max_width and format:
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
                
            
                print_line(line, color, max_width, format)
                count += 1
            except EOFError as err:
                break

        print_end()
    else:
        print("ERRO!")
        program_usage()


main()
