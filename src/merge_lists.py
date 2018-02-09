import random


def merge_lists():
    sorted_list = []
    first_length = 0
    second_length = 0
    while first_length < len(list_one) or second_length < len(list_two):
        if second_length == len(list_two) or \
                (second_length < len(list_two) and first_length < len(
                    list_one) and list_one[first_length] <
                    list_two[second_length]):
            sorted_list.append(list_one[first_length])
            first_length += 1
        elif first_length == len(list_one) or \
                (first_length < len(list_one) and second_length < len(
                    list_two) and list_one[first_length] >
                    list_two[second_length]):
            sorted_list.append(list_two[second_length])
            second_length += 1
        else:
            sorted_list.append(list_one[first_length])
            sorted_list.append(list_two[second_length])
            first_length += 1
            second_length += 1
    print(sorted_list)


list_one = sorted([random.randint(0, 40) * i for i in range(40)])
list_two = sorted([random.randint(0, 50) * i for i in range(50)])
merge_lists()
