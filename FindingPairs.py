def find_pairs(numbers, sum_value):
    values = occurrence(numbers)
    pairs = {}
    for i in numbers:
        if (sum_value - i) in values:
            if i != sum_value - i or (i == sum_value - i and values[i] > 1):
                if i not in pairs and (sum_value - i) not in pairs:
                    pairs[i] = sum_value - i
    return pairs


def occurrence(numbers):
    values = {}
    for i in numbers:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1
    return values
