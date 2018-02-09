import os
import heapq


def visit(l_string, string, b_string):
    n_string = ''.join(string[i] for i in l_string if i != -1)
    if int(n_string) % 8 == 0:
        b_string.append(n_string)


def permute(l_string, b_string, string, index):
    if index == 0:
        visit(l_string, string, b_string)
    else:
        for k in range(len(l_string)):
            if l_string[k] == -1:
                l_string[k] = index - 1
                permute(l_string, b_string, string, index - 1)
                l_string[k] = -1


def b_permute(l_string, b_string, string, index):
    if index == 0:
        visit(l_string, string, b_string)
    else:
        for k in range(index):
            l_string[k], l_string[index-1] = l_string[index-1], l_string[k]
            b_permute(l_string, b_string, string, index-1)
            l_string[k], l_string[index - 1] = l_string[index - 1], l_string[k]


def build_suffixes(string):
    return [string[i:len(string)] for i in range(len(string))]


def get_sim_number(next_str, string):
    return len(os.path.commonprefix([next_str, string]))


def sim_index(string):
    suffixes = build_suffixes(string)
    return sum([get_sim_number(suffix, string) for suffix in suffixes])


def min_heap():
    heap = []
    numbers = [11, 13, 9, 5, 7, 100, 12, 200]
    for i in numbers:
        heapq.heappush(heap, i)
    print(heap)


def max_heap():
    heap = []
    numbers = [11, 13, 9, 5, 7, 100, 12, 200]
    for i in numbers:
        heapq.heappush(heap, i * -1)
    print([i * -1 for i in heap])


def permute_phone_numbers(numbers, curr, output, n):
    if curr == n:
        print(output)
        return
    for i in range(0, len(tel_data[numbers[curr]])):
        output.append(tel_data[numbers[curr]][i])
        permute_phone_numbers(numbers, curr + 1, output, n)
        if numbers[curr] == 0 or numbers[curr] == 1:
            return


def max_sum_sub_array(array):
    max_curr = array[0]
    max_global = array[0]
    for i in range(len(array)):
        max_curr = max(array[i], max_curr + array[i])
        if max_curr > max_global:
            max_global = max_curr
    return max_global

min_heap()
max_heap()


tel_data = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
