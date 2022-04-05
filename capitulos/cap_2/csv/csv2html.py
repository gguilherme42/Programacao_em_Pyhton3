import sys

MAX_WIDTH = 100


def print_start(): 
    print("<table border='1'>")


def print_line(line: str, color: str, maxwidth: int): 
    print(f"<tr bgcolor={color}>")
    
    fields = extract_fields(line)

    for field in fields:
        if not field:
            print("<td></td>")
        else:
            number = field.replace(",","")
            try:
                x = float(number)
                print(f"<td align='rigth'>{round(x):d}</td>")
            except ValueError:
                field = field.title()
                field = field.replace(" AND ", " and ")
                field = escape_html(field)
                if len(field) <= MAX_WIDTH:
                    print(f"<td>{field}</td>")
                else:
                    print(f"<td>{field[:MAX_WIDTH]}...</td>")
                print("</tr")


def extract_fields(line: str) -> [str]: 
    result = []
    field = ""
    quote = None

    for c in line:
        if c in "\"'":
            if quote is None:           # start of quoted string
                quote = c
            elif quote == c:            # end of quoted string
                quote = None
            else:
                field += c              # other quote insed quoted string
            continue
        if quote is None and c == ",":  # end of a field
            result.append(field)
            field = ""
        else:
            field += c                  
        if field:
            result.append(field)        # adding last field

    return result


def escape_html(field: str) -> str: 
    result = field.replace("&", "&amp;")
    result = field.replace("<","&lt;")
    result = field.replace(">","&gt;")
    return result


def print_end(): 
    print("</table>")


def main():
    if len(sys.argv) > 1:
        print(f"Usage: script >  output_file. Argv: {len(sys.argv)}")
        sys.exit()



    print_start()
    count = 0

    while True:
        try:
            line = input()
            if count == 0:
                color = "lightgreen"
            elif count % 2:
                color = "white"
            else:
                color = "lightyellow"

            print_line(line, color, MAX_WIDTH)

            count += 1
        except EOFError:
            break
        except KeyboardInterrupt:
            break

    print_end()

    
main()
