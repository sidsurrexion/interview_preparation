billion_numbers = [i for i in range(1000000000)]
collect_mappers = []
mapper = set()
count = 0
has_found = False
for i in billion_numbers:
    count += 1
    if i not in mapper:
        mapper.add(i)
    else:
        print(i)
        has_found = True
        break
    if count != 0 and count % 1000000 == 0:
        collect_mappers.append(mapper)
        mapper = set()
if not has_found:
    for i in range(len(collect_mappers) - 1):
        for j in range(len(collect_mappers)[i:]):
            for k in collect_mappers[i]:
                if k in collect_mappers[j]:
                    print(k)
                    break
