import sys

string = input()
mapper = {}
for i in range(len(string)):
    if string[i] in mapper:
        mapper[string[i]].append(i)
    else:
        mapper[string[i]] = [i]
min_index = sys.maxsize
first_repeating_character = ''
for key in mapper.keys():
    if len(mapper[key]) == 1:
        if mapper[key][0] < min_index:
            min_index = mapper[key][0]
            first_repeating_character = key
print(first_repeating_character)
