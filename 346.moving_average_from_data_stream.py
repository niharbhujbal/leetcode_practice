from collections import deque


class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.q = deque()
        self.total = 0
        self.q_size = 0

    def next(self, val: int) -> float:
        if self.q_size == self.size:
            self.total -= self.q.popleft()
            self.q_size -= 1

        self.q.append(val)
        self.total += val
        self.q_size += 1
        return self.total / self.q_size


# just stroe max size and double ended queue size, total sum of queue
# every time we add element check if the size is max size then pop one element from left and subtract it from total and decrese size of queue
# add value in queue increse the size and retun the division
