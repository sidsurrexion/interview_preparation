import sys


def kadane(input_data):
    result = [sys.maxsize * -1, 0, -1]
    current_max = 0
    start = 0
    for z in range(len(input_data)):
        current_max += input_data[z]
        if current_max < 0:
            current_max = 0
            start = z + 1
        elif current_max > result[0]:
            result[0] = current_max
            result[1] = start
            result[2] = z
    if result[2] == -1:
        result[0] = input_data[0]
        for z in range(len(input_data)):
            if input_data[z] > result[0]:
                result[0] = input_data[z]
                result[1] = z
                result[2] = z
    return result


data = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
columns = len(data[0])
rows = len(data)
maximum_sum = sys.maxsize * -1
left = 0
top = 0
right = 0
bottom = 0
for i in range(columns):
    tmp = [0 for l in range(rows)]
    for j in range(i, columns):
        for k in range(rows):
            tmp[k] += data[k][j]
        data_result = kadane(tmp)
        if data_result[0] > maximum_sum:
            maximum_sum = data_result[0]
            left = i
            top = data_result[1]
            right = j
            bottom = data_result[2]
