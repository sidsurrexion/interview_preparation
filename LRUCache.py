import heapq


class PQ(object):
    def __init__(self):
        self.heap = []

    def offer(self, item):
        heapq.heappush(self.heap, item)

    def poll(self):
        return heapq.heappop(self.heap)

    def replace(self, item):
        temp = []
        while self.heap:
            element = self.poll()
            if element[1] == item[1]:
                element = item
            temp.append(element)
        self.heap = temp
        heapq.heapify(self.heap)


class LRU(object):
    def __init__(self, size):
        self.size = size
        self._lru_mapper = {}
        self._count_mapper = {}
        self.count = 0
        self.queue = PQ()

    def add(self, item):
        self.count += 1
        if len(self._lru_mapper) == self.size \
                and item[0] not in self._lru_mapper:
            element = self.queue.poll()
            self._count_mapper.pop(element[1], None)
            self._lru_mapper.pop(element[1], None)
        self._lru_mapper[item[0]] = item[1]
        self.add_item_to_queue(item)
        self._count_mapper[item[0]] = self.count

    def add_item_to_queue(self, item):
        if item[0] in self._count_mapper:
            self.queue.replace((self.count, item[0]))
        else:
            self.queue.offer((self.count, item[0]))

    def print_mapper(self):
        for key, value in self._lru_mapper.items():
            print(str(key) + ',' + value)


lru = LRU(3)
lru.add((1, 'a'))
lru.add((2, 'c'))
lru.add((3, 'd'))
lru.add((2, 'd'))
lru.add((3, 'e'))
lru.add((4, 'f'))
lru.add((5, 'g'))
lru.print_mapper()
