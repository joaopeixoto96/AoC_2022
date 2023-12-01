import os
file_path = os.path.join('Advent of Code','data_day1.txt')

file_input = open(file_path)
data = [i for i in file_input.read().strip().split('\n')]

maior = []
soma = 0

for item in data:
    if item == '':
        maior.append(soma)
        soma = 0
    else:
        soma += int(item)
maior.sort(reverse=True)
print(maior)
