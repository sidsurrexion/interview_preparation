def maximum_individual_sum(numbers, k):
    _sum = 0
    weight = []
    for i, x in enumerate(numbers):
        _sum += x
        if i >= k:
            _sum -= numbers[i-k]
        if i >= k - 1:
            weight.append(_sum)
    left = [0] * len(weight)
    best = 0
    for i in range(len(weight)):
        if weight[i] > weight[best]:
            best = i
        left[i] = best
    right = [0] * len(weight)
    best = len(weight) - 1
    for i in range(len(weight), -1, -1):
        if weight[i] >= weight[best]:
            best = i
        right[i] = best
    indices = None
    for j in range(k, len(weight) - k):
        i, k = left[j-k], right[j+k]
        if indices is None or weight[i] + weight[j] + weight[k] > \
                weight[indices[0]] + weight[indices[1]] + weight[indices[2]]:
            indices = i, j, k
    return indices
