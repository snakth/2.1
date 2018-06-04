
with open('text.txt') as f:
    print(f.read())

print('Файл закрыт? {}'.format(f.closed))
