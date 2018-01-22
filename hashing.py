class HashTable(object):
    def __init__(self):
        self.DEFAULT = 1000
        self.value_list = []
        self.keys = []
        self.initialize_values()

    def initialize_values(self):
        itr = self.DEFAULT
        while itr > 0:
            self.value_list.append(0)
            self.keys.append(0)
            itr -= 1

    def add(self, key, value):
        index = hash(key) & self.DEFAULT
        self.value_list[index] = value
        self.keys[index] = key

    def delete(self, key):
        index = hash(key) & self.DEFAULT
        self.value_list[index] = 0
        self.keys[index] = 0

    def get(self, key):
        return self.value_list[hash(key) & self.DEFAULT]

    def get_all(self):
        for i in range(len(self.keys)):
            if self.keys[i] != 0:
                print(self.keys[i], self.value_list[i])
