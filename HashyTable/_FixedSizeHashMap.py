class _FixedSizeHashMap:
    def __init__(self, array_size: int = 10):
        self.table = list()

        for x in range(array_size):
            self.table.append(list())
        self.length = 0

    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        self.pop(key, None)

        bucket_list.append((key, value))
        self.length += 1

    def __setitem__(self, key, value):
        self.insert(key, value)

    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for item in bucket_list:
            if item[0] == key:
                return item[1]
        else:
            raise KeyError

    def __getitem__(self, item):
        return self.search(item)

    def __contains__(self, item):
        try:
            value = self.search(item)
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

    def copy(self):
        h = _FixedSizeHashMap()

        for (key, value) in self.items():
            h.insert(key, value)

        return h

    def items(self):
        result = list()
        for bucket_list in self.table:
            result.extend(bucket_list)

        return result

    def keys(self):
        return [x[0] for x in self.items()]

    def values(self):
        return [x[1] for x in self.items()]