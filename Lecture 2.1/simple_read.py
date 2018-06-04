#
f = open('text.txt', encoding='utf8')

# print(f.read())

# print(f.readline().strip())
# print(f.readline().strip())

for l in f:
    print(l.strip())
    print('=========')

f.close()



