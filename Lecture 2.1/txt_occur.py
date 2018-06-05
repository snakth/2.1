
count = 0

with open('text.txt') as f:
    for l in f:
        if 'Привет' in l and 'Мир' in l:
            count += 1

print(count)
