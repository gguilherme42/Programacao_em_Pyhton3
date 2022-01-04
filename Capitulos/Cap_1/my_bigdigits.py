import sys

zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]

one =  [" * ",
        "** ",
        " * ",
        " * ",
        " * ",
        " * ",
        "***"]

two =  [" *** ",
        "*   *",
        "*  * ",
        "  *  ",
        " *   ",
        "*    ",
        "*****"]

three = []

four = []

five = []

six  = []

seven = []

eight = []

nine = [" ****",
        "*   *",
        "*   *",
        " ****",
        "    *",
        "    *",
        "    *",]

digits = [zero, one, two, three, four, five,
        six, seven, eight, nine]


try:
    input_digits = sys.argv[1]
    print(f"----> {sys.argv[1]}")
    row = 0
    while row < 7:
        line = ""
        column = 0
        while column < len(input_digits):
            number = int(input_digits[column])
            input_digits = digits[number]
            line += input_digits[row] + ""
            column += 1
        print(line)
        row += 1

except IndexError:
    print("Usage: my_bigdigits.py <number>")

except ValueError as err:
    print(f"{err} in {input_digits}")
