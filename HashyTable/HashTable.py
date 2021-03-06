

class HashTable:
    def __init__(self, array_size: int = 10):
        self.table = list()
        self.capacity = array_size

        for x in range(array_size):
            self.table.append(list())
        self.length = 0

    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        self.pop(key, None)

        bucket_list.append((key, value))
        self.length += 1

        if len(bucket_list) > 10:
            self.resize(self.capacity * 2)

    def __setitem__(self, key, value):
        self.insert(key, value)

    def get(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for item in bucket_list:
            if item[0] == key:
                return item[1]
        else:
            raise KeyError

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        try:
            value = self.get(item)
            return True
        except KeyError:
            return False

    def clear(self):
        for i in range(len(self.table)):
            self.table[i] = []
        self.length = 0

    def pop(self, key, *args):
        for bl in range(len(self.table)):
            for i in range(len(self.table[bl])):
                if self.table[bl][i][0] == key:
                    result = self.table[bl][i][0]
                    del self.table[bl][i]
                    self.length -= 1
                    return result
        else:
            if len(args) == 0:
                raise KeyError
            else:
                return args[0]

    def popitem(self):
        return self.pop(self.keys().__next__())

    def copy(self):
        h = HashTable()

        for (key, value) in self.items():
            h.insert(key, value)

        return h

    def items(self):
        return (item for bucket_list in self.table for item in bucket_list)

    def keys(self):
        return (x[0] for x in self.items())

    def values(self):
        return (x[1] for x in self.items())

    def update(self, iterable):
        for (key, value) in iterable.items():
            self.insert(key, value)

    def setdefault(self, key, value=None):
        if key in self:
            return self[key]
        else:
            self.insert(key, value)
            return value

    def fromkeys(self, keys, value=None):
        result = HashTable()

        for key in keys:
            result.insert(key, value)

        return result

    def __len__(self):
        return self.length

    def __str__(self):
        result = '{'
        result += ", ".join([f'{key}: {value}' for (key, value) in self.items()])
        result += '}'
        return result

    def __delitem__(self, key):
        self.pop(key)

    def __iter__(self):
        return self.keys()

    def resize(self, array_size):
        new_hash = HashTable(array_size)

        for (key, value) in self.items():
            new_hash.insert(key, value)

        self.table = new_hash.table
        self.length = new_hash.length
        self.capacity = new_hash.capacity
