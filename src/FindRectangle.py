

def create_rectangle(rows, columns):
    return [[input() for j in range(columns)] for i in range(rows)]


def get_horizontal_ones(matrix):
    stars = {}
    if not matrix:
        return None
    row_num = len(matrix)
    col_num = len(matrix[0])
    for i in range(row_num):
        for j in range(col_num):
            if matrix[i][j] == '*':
                if i in stars:
                    stars[i].append(j)
                else:
                    stars[i] = []