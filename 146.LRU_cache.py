class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.usage = []
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.usage.remove(key)
            self.usage.append(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            self.cache[key] = value
            self.usage.remove(key)
            self.usage.append(key)
        elif len(self.cache) < self.capacity:
            self.cache[key] = value
            self.usage.append(key)
        else:
            del self.cache[self.usage.pop(0)]
            self.cache[key] = value
            self.usage.append(key)


# we can use doubly linked list to story how the elements are used recently


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
