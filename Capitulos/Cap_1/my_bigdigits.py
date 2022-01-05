import sys

# The other numbers are empty because I'm lazy
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
    print(f"----> {len(sys.argv[1])}")
    
    for row in range(7):
        line = ""

        for column in range(len(input_digits)):  
            number = int(input_digits[column])
            selected_digit = digits[number]
            line += selected_digit[row] + "  "
        
        print(line)
    

except IndexError:
    print("Usage: my_bigdigits.py <number>")

except ValueError as err:
    print(f"{err} in {input_digits}")
