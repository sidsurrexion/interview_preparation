number = int(input())
f_numbers = []
for i in range(number):
    if i == 0:
        f_numbers.append(0)
    elif i == 1:
        f_numbers.append(1)
    else:
        f_numbers.append(f_numbers[i-1] + f_numbers[i-2])
print(f_numbers)
