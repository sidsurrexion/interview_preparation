def string_offset(string, path):
    offset_map = []
    with open(path) as file:
        index = 0
        for line in file:
            if string in line:
                offset_map.append((index, line.find(string)))
            index += 1
    return offset_map


def naive_string_matching(input_string, test_string):
    if len(input_string) > len(test_string):
        return -1
    for i in range(len(test_string) - len(input_string)):
        if input_string == test_string[i:i+len(input_string)]:
            return i


def get_hash(input_string):
    return sum(ord(i) for i in input_string)


def ruben_karp_matching(input_string, test_string):
    if len(input_string) > len(test_string):
        return -1
    hi = get_hash(input_string)
    ht = get_hash(test_string[0:len(input_string)])
    if hi == ht and input_string == test_string[0:len(input_string)]:
        return 0
    else:
        for i in range(len(input_string), len(test_string)):
            ht -= test_string[i - len(input_string)]
            ht += test_string[i]
            if hi == ht and input_string == test_string[i:i+len(input_string)]:
                return i


def visit(list_string, string):
    print(''.join([string[i] for i in list_string if i != -1]))


def permute(list_string, string, index):
    if index == 0:
        visit(list_string, string)
    else:
        for k in range(len(list_string)):
            if list_string[k] == -1:
                list_string[k] = index - 1
                permute(list_string, string, index - 1)
                list_string[k] = -1


def better_permute(list_string, string, index):
    if index == 0:
        visit(list_string, string)
    else:
        for k in range(index):
            list_string[k], list_string[index - 1] = list_string[index -
                                                                 1], \
                                                     list_string[k]
            better_permute(list_string, string, index - 1)
            list_string[k], list_string[index - 1] = list_string[index -
                                                                 1], \
                                                     list_string[k]


def lcs(first_string, second_string, first_length, second_length):
    if first_length == 0 or second_length == 0:
        return 0
    elif first_string[first_length - 1] == second_string[second_length - 1]:
        return 1 + lcs(first_string, second_string, first_length - 1,
                       second_length - 1)
    else:
        return max(lcs(first_string, second_string, first_length,
                       second_length - 1), lcs(first_string, second_string,
                                               first_length - 1,
                                               second_length))


def lcs_alternative(first_string, second_string):
    m = len(first_string)
    n = len(second_string)
    l = [[0] * (n + 1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 and j == 0:
                l[i][j] = 0
            elif first_string[i-1] == second_string[j-1]:
                l[i][j] = 1 + l[i-1][j-1]
            else:
                l[i][j] = max(l[i][j-1], l[i-1][j])
    return l[m][n]


def lcs_string(first_string, second_string):
    m = len(first_string)
    n = len(second_string)
    l = [[0] * (n+1) for i in range(m+1)]
    result = 0
    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                l[i][j] = 0
            elif first_string[i-1] == second_string[j-1]:
                l[i][j] = 1 + l[i-1][j-1]
                result = max(result, l[i][j])
            else:
                l[i][j] = 0
    return result


def lis(sequence):
    length = len(sequence)
    l = [1] * length
    for i in range(1, length):
        for j in range(i):
            if sequence[i] < sequence[j] and l[i] < l[j] + 1:
                l[i] = l[j] + 1
    maximum = 1
    for i in l:
        maximum = max(maximum, i)
    return maximum


def edit_distance(first_string, second_string):
    m = len(first_string)
    n = len(second_string)
    d = [[0] * (n+1) for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                d[i][j] = j
            elif j == 0:
                d[i][j] = i
            elif first_string[i-1] == second_string[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = 1 + min(d[i][j-1], d[i-1][j], d[i-1][j-1])
    return d[m][n]


def check_permute(string):
    mapper = {}
    str_length = 0
    for i in string:
        str_length += 1
        if i != ' ':
            if i in mapper:
                mapper[i] = 1
            else:
                mapper[i] += 1
    count = 0
    for value in mapper.values():
        count += value
    if str_length % 2 == 0 and count % 2 == 0:
        return True
    elif str_length % 2 != 0 and count % 2 != 0:
        return True
    return False


def shift_matrix(matrix):
    tmp_matrix = []
    row = len(matrix)
    column = len(matrix[0])
    for i in range(column):
        count = row - 1
        tmp_mat = []
        while count >= 0:
            tmp_mat.append(matrix[count][i])
            count -= 1
        tmp_matrix.append(tmp_mat)
    return tmp_matrix


def column_zero(matrix, column):
    for i in matrix:
        i[column] = 0
    return matrix


def zero_matrix(matrix):
    tmp_matrix = [x[:] for x in matrix]
    for i in range(len(tmp_matrix)):
        for j in range(len(tmp_matrix[0])):
            if tmp_matrix[i][j] == 0:
                matrix[i] = [0] * len(tmp_matrix[0])
                matrix = column_zero(matrix, j)
    return matrix


def urlify(string):
    return ''.join(["%20" if i == " " else i for i in string.strip()])


s = "abc"
l = [-1 for i in s]
permute(l, s, len(s))
better_permute([i for i in range(len(s))], s, len(s))
mat = [[1] * 5 for j in range(5)]
mat[2][2] = 0
print(urlify("Mr John Smith  "))
print(zero_matrix(mat))
d_matrix = [[0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [1, 0, 0, 0],
            [3, 0, 0, 0]]
print(shift_matrix(d_matrix))
