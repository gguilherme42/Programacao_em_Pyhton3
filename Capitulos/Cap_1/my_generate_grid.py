import random

def get_int(msg, minimum, default: int=None):
    while True:
        try:
            number_input = input(msg)
            if not number_input and default:
                return default
            number_input = int(number_input)

            if number_input < minimum:
                print(f"must be >= {minimum}")
            else:
                return number_input
        except ValueError as err:
            print(err)


def print_grid_of_random_numbers(rows, columns, maximum, minimum):
    for row in range(rows):
        line = ""
        for column in range(columns):
            random_integer = random.randint(minimum, maximum)
            random_integer_to_print = str(random_integer)

            while len(random_integer_to_print) < 10:
                random_integer_to_print += f" {random_integer_to_print}"
            
            line += random_integer_to_print
        
        print(line)



rows_input = get_int("rows: ", 1)
columns_input = get_int("columns: ", 1)
minimum = get_int("minimum (or ENTER for 0):  ", -1000000, 0)

default_number = 1000 if 1000 > minimum else 2 * minimum

maximum = get_int(f"maximum (or ENTER for {default_number}): ", minimum, default_number)

print_grid_of_random_numbers(rows_input, columns_input, maximum, minimum)