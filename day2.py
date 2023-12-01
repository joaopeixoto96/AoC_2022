import os
import pandas as pd
file_path = os.path.join('Advent of Code','data_day2.txt')

df = pd.read_csv(file_path)
results = []
points = []
pedra = 1
papel = 2
tesoura = 3
vitoria = 6
empate = 3
derrota = 0

'X= pedra, Y= papel, Z= tesoura'

# for index, row in df.iterrows():
#     if row['Oponent'] == 'A' and row['Self'] == 'X':
#         results.append('E')
#         points.append(pedra+empate)
#     elif row['Oponent'] == 'A' and row['Self'] == 'Y':
#         results.append('V')
#         points.append(papel+vitoria)
#     elif row['Oponent'] == 'A' and row['Self'] == 'Z':    
#         results.append('D')
#         points.append(tesoura+derrota)

#     elif row['Oponent'] == 'B' and row['Self'] == 'X':
#         results.append('D')
#         points.append(pedra+derrota)
#     elif row['Oponent'] == 'B' and row['Self'] == 'Y':
#         results.append('E')
#         points.append(papel+empate)
#     elif row['Oponent'] == 'B' and row['Self'] == 'Z':    
#         results.append('V')
#         points.append(tesoura+vitoria)

#     elif row['Oponent'] == 'C' and row['Self'] == 'X':
#         results.append('V')
#         points.append(pedra+vitoria)
#     elif row['Oponent'] == 'C' and row['Self'] == 'Y':
#         results.append('D')
#         points.append(papel+derrota)
#     elif row['Oponent'] == 'C' and row['Self'] == 'Z':    
#         results.append('E')
#         points.append(tesoura+empate)

'X = derrota, Y = empate, Z= vitoria'


for index, row in df.iterrows():
    if row['Oponent'] == 'A' and row['Self'] == 'X':
        results.append('D')
        points.append(tesoura+derrota)
    elif row['Oponent'] == 'A' and row['Self'] == 'Y':
        results.append('E')
        points.append(pedra+empate)
    elif row['Oponent'] == 'A' and row['Self'] == 'Z':    
        results.append('V')
        points.append(papel+vitoria)

    elif row['Oponent'] == 'B' and row['Self'] == 'X':
        results.append('D')
        points.append(pedra+derrota)
    elif row['Oponent'] == 'B' and row['Self'] == 'Y':
        results.append('E')
        points.append(papel+empate)
    elif row['Oponent'] == 'B' and row['Self'] == 'Z':    
        results.append('V')
        points.append(tesoura+vitoria)

    elif row['Oponent'] == 'C' and row['Self'] == 'X':
        results.append('D')
        points.append(papel+derrota)
    elif row['Oponent'] == 'C' and row['Self'] == 'Y':
        results.append('E')
        points.append(tesoura+empate)
    elif row['Oponent'] == 'C' and row['Self'] == 'Z':    
        results.append('V')
        points.append(pedra+vitoria)


print(sum(points))        


