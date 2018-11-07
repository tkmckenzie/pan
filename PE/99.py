import numpy as np

f = open('data/99.txt', 'r')
data = [line.strip().split(',') for line in f]
data = [[int(line[0]), int(line[1])] for line in data]
f.close()

max_line = None
max_value = 0
for line_no in range(len(data)):
    line = data[line_no]
    value = line[1] * np.log(line[0])
    if value > max_value:
        max_value = value
        max_line = line_no

print(max_line + 1)
