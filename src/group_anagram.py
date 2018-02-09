words = input().split(' ')
word_mapper = {}
for word in words:
    sorted_word = ''.join(sorted(word.lower()))
    if sorted_word in word_mapper:
        word_mapper[sorted_word].append(word)
    else:
        word_mapper[sorted_word] = [word]
for word_list in word_mapper.values():
    print(word_list)
