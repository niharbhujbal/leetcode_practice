from sortedcontainers import SortedDict


class TimeMap:
    def __init__(self):
        self.key_time_map = {}

    def set(self, key, value, timestamp):
        # If the 'key' does not exist in dictionary.
        if not key in self.key_time_map:
            self.key_time_map[key] = SortedDict()

        # Store '(timestamp, value)' pair in 'key' bucket.
        self.key_time_map[key][timestamp] = value

    def get(self, key, timestamp):
        # If the 'key' does not exist in dictionary we will return empty string.
        if not key in self.key_time_map:
            return ""

        it = self.key_time_map[key].bisect_right(timestamp)
        # If iterator points to first element it means, no time <= timestamp exists.
        if it == 0:
            return ""

        # Return value stored at previous position of current iterator.
        return self.key_time_map[key].peekitem(it - 1)[1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
