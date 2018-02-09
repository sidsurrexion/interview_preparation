def intersect(elements):
    main = set()
    for l in elements:
        if not main:
            main = set([i for i in l])
        else:
            main = main.intersection(set([i for i in l]))
    return main


l = [input(), input(), input()]
print(intersect(l))
