import os
import numpy as np

file_path = os.path.join('Advent of Code','data_day8.txt')
file_input = open(file_path)
data = [i for i in file_input.read().strip().split('\n')]
# print(data)

trees = np.zeros((len(data), len(data[0])), dtype=int)
for i, line in enumerate(data):
    trees[i, :] = np.array(list(line))

visible_trees = 2*len(data[0]) + 2 *(len(data)-2)

for i in range(1, trees.shape[0]-1):
    for j in range(1, trees.shape[1]-1):
        columns = trees[:,j] - trees[i,j]
        rows = trees[i,:] - trees[i,j]
        routes = [rows[:j], rows[j+1:], columns[:i],columns[i+1:]]
        if sum(list(map(lambda route: (route<0).all(), routes))) > 0:
            visible_trees += 1
print(visible_trees)

scenic_scores = np.zeros((len(data), len(data[0])), dtype=int)

def compute_scenic_score(route):
    big_trees_array = list(route >= 0)
    if True in big_trees_array:
        return big_trees_array.index(True) + 1
    else:
        return len(big_trees_array)

# iterate over trees
for i in range(1, trees.shape[0]-1):
    for j in range(1, trees.shape[1]-1):
        tree_column = trees[:, j] - trees[i, j]
        tree_row = trees[i, :] - trees[i, j]
        # left, right, up, down
        routes = [tree_row[j-1::-1], tree_row[j+1:], tree_column[i-1::-1], tree_column[i+1:]]
        scenic_scores[i,j] = np.prod(list(map(compute_scenic_score, routes)))
    
np.max(scenic_scores)

print(np.max(scenic_scores))

