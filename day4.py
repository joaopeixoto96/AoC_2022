import os
file_path = os.path.join('Advent of Code','data_day4.txt')
file_input = open(file_path)
data = [i for i in file_input.read().strip().split('\n')]



number_of_contains = 0
for assignment_pair in data:
    first_range, second_range = assignment_pair.split(',')
    start_a, end_a = map(int, first_range.split('-'))
    start_b, end_b = map(int, second_range.split('-'))    
    if start_a <= start_b and end_a >= end_b or start_b <= start_a and end_a <= end_b:
        number_of_contains += 1

print(number_of_contains) 

overlap = 0
for assignment_pair in data:
    first_range, second_range = assignment_pair.split(',')
    start_a, end_a = map(int, first_range.split('-'))
    start_b, end_b = map(int, second_range.split('-'))
    if start_a in range(start_b, end_b+1) or end_a in range(start_b, end_b+1) or  start_b in range(start_a, end_a+1) or end_b in range(start_a, end_a+1):
        overlap += 1
        
print(overlap)