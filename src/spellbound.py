def check_if_seq_exists(input_string, word):
    count = 0
    for s in input_string:
        if count == len(word):
            return True
        if s == word[count]:
            count += 1
    return count == len(word)


def init_method():
    pass

q = int(input().strip())
for i in range(q):
    string = input().strip()
    if check_if_seq_exists(string, 'hackerrank'):
        print("YES")
    else:
        print("NO")
