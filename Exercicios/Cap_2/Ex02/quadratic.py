import math
import cmath
import sys


def get_float(msg, allow_zero=True):
    while True:
        try:
            float_number = float(input(msg))
            if not allow_zero and abs(float_number) < sys.float_info.epsilon:
                print('Zero is not allowed')
                continue
        except ValueError as err:
            print(err)
        else:
            return float_number


print(
    'ax\N{SUPERSCRIPT TWO} + bx + c = 0')  # ax² + bx + c = 0
a = get_float('Enter a: ', False)
b = get_float('Enter b: ')
c = get_float('Enter c: ')

x1 = x2 = None

discriminant = (b ** 2) - (4 * a * c)
if discriminant == 0:
    x1 = - (b / (2 * a))
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else:
        root = cmath.sqrt(discriminant)
    x1 = (- b + root) / (2 * a)
    x2 = (- b - root) / (2 * a)

equation = f"""{a:.0f}x² {'+' if b > 0 else '-'} {abs(b):.0f}x {'+' if c > 0 else '-'} {abs(c):.0f} = 0
-> x = {x1:.2f} 
"""
if x2 is not None:
    equation += f'or x = {x2:.2f}'

print(equation)
