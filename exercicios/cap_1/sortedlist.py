n = []
while True:
    try:
        i = int(input('Enter a number or Enter to finish: '))
    except:
        break
    else:
        n.append(i)

fim = len(n)
# Bubble Sort ↓
while fim > 1:
    trocou = False
    x = 0
    while x < fim - 1:
        if n[x] > n[x + 1]:
            trocou = True
            temp = n[x]
            n[x] = n[x + 1]
            n[x + 1] = temp
        x += 1

    if not trocou:
        break
    fim -= 1




print(f'Numbers: {n}')
print(f'''Count: {len(n)}
Sum: {sum(n)}
Highest: {max(n)}
Lowest: {min(n)}
Mean: {sum(n)/len(n)}
''')

