import cmath, math, sys

def get_float(msg: str, allow_zero: bool):
    result = None
    
    while result is None:
        try:
            result = float(input(msg))
            if not allow_zero and abs(result) < sys.float_info.epsilon:
                print("Zero is not allowed")
                result = None
        except ValueError as err:
            print(err)
    
    return result

print("ax\N{SUPERSCRIPT TWO} + bx + c = 0")
a = get_float("Enter a: ", False)
b = get_float("Enter b: ", True)
c = get_float("Enter c: ", True)

x1 = x2 = None

discriminant = (b ** 2) - (4 * a * c)

if discriminant == 0:
    x1 =  - (b / (2 * a))
else:
    if discriminant > 0:
        root = math.sqrt(discriminant)
    else:
        root = cmath.sqrt(discriminant)
    x1 = (-b + root) / (2 * a)
    x2 = (-b - root) / (2 * a)

equation = (f"{a}x\N{SUPERSCRIPT TWO} + {b}x + {c} = 0 "
            f"\N{RIGHTWARDS ARROW} x = {x1}")

if x2:
    equation += f" or x = {x2}"

print(equation)