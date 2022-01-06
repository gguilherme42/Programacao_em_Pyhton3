def median(list):
    center_value = len(list) // 2
    return list[center_value]


def sort_list(list_to_order):
    while True:
        changed = False
        for index, value in enumerate(list_to_order):
            if not(index + 1 == len(list_to_order)):
                if value > list_to_order[index + 1]:
                    greater_value = value
                    next_lower_value = list_to_order[index + 1]
                    list_to_order[index] = next_lower_value
                    list_to_order[index + 1] = greater_value
                    changed = True
        if not changed:
            break
    return list_to_order


number_list = []
while True:
    try:
        input_number = float(input('Enter a number or Enter to finish: '))
    except:
        break
    else:
        number_list.append(input_number)


print(f'Numbers unsorted: {number_list}')


print(f'Numbers sorted: {number_list}')
print(f'''Count: {len(number_list)}
Sum: {sum(number_list)}
Highest: {max(number_list)}
Lowest: {min(number_list)}
Mean: {sum(number_list)/len(number_list):.2f}
Median: {median(sort_list(number_list))}
''')

