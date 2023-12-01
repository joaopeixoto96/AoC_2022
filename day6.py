import os
file_path = os.path.join('Advent of Code','data_day6.txt')
with open(file_path,'r') as data:
    lines = data.readline().strip()

for i in range(len(lines)):
    if len(set(lines[i:i+4])) == 4:
        result_1 = i + 4
        break

for i in range(len(lines)):
    if len(set(lines[i:i+14])) == 14:
        result_2 = i + 14
        break

print(result_1, result_2)