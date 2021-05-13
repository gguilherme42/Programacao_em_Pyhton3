def median(list):
    center_value = int(len(list) / 2)
    return list[center_value]


def sort_list(list):
    while True:
        changed = False
        for index, value in enumerate(list):
            if not(index + 1 == len(list)):
                if value > list[index + 1]:
                    greater_value = value
                    next_lower_value = list[index + 1]
                    list[index] = next_lower_value
                    list[index + 1] = greater_value
                    changed = True
        if not changed:
            break


number_list = []
while True:
    try:
        input_number = float(input('Enter a number or Enter to finish: '))
    except:
        break
    else:
        number_list.append(input_number)


print(f'Numbers unsorted: {number_list}')
sort_list(number_list)

print(f'Numbers sorted: {number_list}')
print(f'''Count: {len(number_list)}
Sum: {sum(number_list)}
Highest: {max(number_list)}
Lowest: {min(number_list)}
Mean: {sum(number_list)/len(number_list):.2f}
Median: {median(number_list)}
''')

