import random
numbers = [i for i in range(1000000000)]
value = random.randint(1000000)
diff = numbers[value] - numbers[value - 1]
count = 0
add = 0
first_num = -1
for i in range(len(numbers)):
    if first_num == -1:
        first_num = numbers[i]
    count += 1
    add += numbers[i]
    if count % 1000 == 0:
        total = (2 * first_num + 999 * diff) * (1000/2)
        if total != add:
            print(abs(total - add))
            break
        first_num = -1
        add = 0
