class _FixedSizeHashMap:
    def __init__(self, array_size: int = 10):
        self.table = list()

        for x in range(array_size):
            self.table.append(list())
        self.length = 0

    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # Remove the key-value pair if already in hashmap
        for i in range(len(bucket_list)):
            if bucket_list[i][0] == key:
                del bucket_list[i]
                break

        bucket_list.append((key, value))

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
