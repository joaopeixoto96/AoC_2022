import os
file_path = os.path.join('Advent of Code','data_day3.txt')
file_input = open(file_path)

data = [i for i in file_input.read().strip().split('\n')]

repeated = []
''' Res for first part '''
# for item in data:
#     length = len(item)
#     half = length // 2
#     first = item[:half]
#     second = item[half:]
#     rep = set(first) & set(second)
#     repeated.append(rep)

''' Res for second part '''

for i in range(0, len(data), 3):
    first = data[i]
    second = data[i+1]
    third = data[i+2]
    rep = set(first) & set(second) & set(third)
    repeated.append(rep)

alpha = 'abcdefghijklmnopqrstuvwxyz'
Alpha = alpha.upper()
points = {letter: index + 1 for index, letter in enumerate(alpha+Alpha)}
ponto = []
for char in repeated:
    char = str(char)
    letra="".join(ch for ch in char if ch.isalnum())
    ponto.append(points[letra])

print(sum(ponto))