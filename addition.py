def addition():
    f_index = len(first) - 1
    s_index = len(second) - 1
    add = []
    carry = 0
    while f_index >= 0 and s_index >= 0:
        summation = int(first[f_index]) + int(second[s_index]) + carry
        add.append(summation % base)
        carry = int(summation / base)
        f_index -= 1
        s_index -= 1
    while f_index >= 0:
        summation = int(first[f_index]) + carry
        add.append(summation % base)
        carry = int(summation / base)
        f_index -= 1
    while s_index >= 0:
        summation = int(second[s_index]) + carry
        add.append(summation % base)
        carry = int(summation / base)
        s_index -= 1
    if carry > 0:
        add.append(carry)
    return ''.join(list(map(str, add[::-1])))
first = input()
second = input()
base = int(input())
print(addition())
