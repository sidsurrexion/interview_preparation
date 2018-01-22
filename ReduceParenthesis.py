import heapq


class Queue(object):
    def __init__(self):
        self.data = []

    def offer(self, item):
        heapq.heappush(self.data, item)

    def poll(self):
        return heapq.heappop(self.data)

    def empty(self):
        return bool(self.data)

    def peek(self):
        return self.data[0]


def is_character_parenthesis(char):
    return char == '(' or char == ')'


def is_string_valid(string):
    count = 0
    for i in range(len(string)):
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
    return count == 0


def remove_parenthesis(string):
    visit = set()
    holder = Queue()
    holder.offer(string)
    visit.add(string)
    level = False
    while not holder.empty():
        string = holder.poll()
        if is_string_valid(string):
            print(string)
            level = True
        if level:
            continue
        for i in range(len(string)):
            if is_character_parenthesis(string[i]):
                tmp = string[0:i] + string[i+1:len(string)]
                if tmp not in visit:
                    visit.add(tmp)
                    holder.offer(tmp)
