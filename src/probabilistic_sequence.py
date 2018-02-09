import sys
import random

numbers = sys.stdin
count = 0
samples = []

for i in numbers:
    count += 1
    if count <= 1000:
        samples.append(int(i))
    else:
        num = random.randint(1000)
        if num / 1000 < 1000 / count:
            samples[num] = int(i)
print(samples)
