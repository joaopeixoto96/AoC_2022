import os
file_path = os.path.join('Advent of Code','data_day10.txt')
# with open(file_path, 'r') as f:
#     lines = f.readlines()
#     commands = [entry.strip() for entry in lines]
# cycle_count = -2
# signal = []
# cycle = []


# for item in commands:
#     if item != 'noop':
#         cmd, num = item.split(' ')
#         # print(f'Command is {cmd} and number is {num}')
#         # signal.append(int(num))
#         cycle_count += 2
#         array = (num,cycle_count)
#         cycle.append(array)
#     else:
#         signal.append(0)
#         cycle_count += 1

# print(cycle)

from itertools import accumulate

f = lambda x: int(x) if x[-1].isdigit() else 0
xs = [*map(f, open(file_path).read().split())]

part1, part2 = 0, '\n'
for i, x in enumerate(accumulate([1]+xs), 1):
    part1 += i*x if i%40==20 else 0
    part2 += '#' if (i-1)%40-x in [-1,0,1] else ' '

print(part1, *part2)



