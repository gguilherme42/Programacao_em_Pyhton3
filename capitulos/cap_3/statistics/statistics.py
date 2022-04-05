import sys
import collections
import math 

Statistcs = collections.namedtuple("Statistics", "mean mode median std_dev")

def read_data(filename: str, numbers: list, frequencies: dict):
    
    for lino, line in enumerate(open(filename, encoding='ascii'), start=1):
        for n in line.split():
            try:
                number = float(n)
                numbers.append(number)
                frequencies[number] += 1
            except ValueError as err:
                print(f"{filename}:{lino}: skipping {n}: {err}")

def calculate_mode(frequencies: dict, maximum_modes: int) -> list:
    highest_frequencie = max(frequencies.values())
    
    result = [number for number, frequency in frequencies.items() 
                    if math.fabs(frequency - highest_frequencie) <= sys.float_info.epsilon
            ]
    
    is_mode_acceptable = 1 <= len(result) <= maximum_modes
    
    return result.sort() if is_mode_acceptable else []

def calculate_median(numbers: list) -> float:
    numbers = sorted(numbers)
    middle = len(numbers) // 2
    result = numbers[middle]
    is_even = len(numbers) % 2 == 0

    return (result + numbers[middle - 1]) / 2 if is_even else result

def calculate_std_dev(numbers: list, mean: float) -> float:
    total = 0 
    for number in numbers:
        total += ((number - mean) ** 2)
    variance = total / (len(numbers) - 1)
    
    return math.sqrt(variance)


def calculate_statistics(numbers: list, frequencies: dict) -> Statistcs:
    mean = sum(numbers) / len(numbers)
    mode = calculate_mode(frequencies, 3)
    median = calculate_median(numbers)
    std_dev = calculate_std_dev(numbers, mean)
    return Statistcs(mean, mode, median, std_dev)

def print_results(count: int, statistics: Statistcs):
    real = "9.2f"
    modeline= ""

    if statistics.mode is not None:
        if len(statistics.mode) == 1:
            modeline = f"mode = {statistics.mode[0]:{real}}\n"
        else:
            mode_to_print = ', '.join([f"{m}:.2f" for m in statistics.mode])
            modeline = f"mode = [{mode_to_print}]\n"
        
    print(f"""\
count     = {count:6}
mean      = {statistics.mean:{real}}
median    = {statistics.median:{real}}
{modeline}\
std. dev  = {statistics.std_dev:{real}}
    """)


def main():

    if len(sys.argv) == 1 or sys.argv[1] in {'-h', '--help'}:
        print(f"usage: {sys.argv[0]} file1 [file2 [...fileN]]")
        sys.exit()
    
    numbers = []
    frequencies = collections.defaultdict(int)

    for filename in sys.argv[1:]:
        read_data(filename, numbers, frequencies)
    
    if numbers:
        statistics = calculate_statistics(numbers, frequencies)
        print_results(len(numbers), statistics)
    else:
        print("No numbers found")

main()