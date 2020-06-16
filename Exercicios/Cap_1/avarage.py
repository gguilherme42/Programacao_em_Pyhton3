n = []
while True:
    try:
        i = float(input('Enter a number or Enter to finish: '))
    except:
        break
    else:
        n.append(i)

print(f'Numbers: {n}')
print(f'''Count: {len(n)}
Sum: {sum(n)}
Highest: {max(n)}
Lowest: {min(n)}
Mean: {sum(n)/len(n)}
''')
