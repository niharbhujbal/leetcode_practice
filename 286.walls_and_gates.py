class Solution:
    def wallsAndGates(self, rooms):
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        gate_pos = []
        visited_set = set()
        for r in range(m):
            for c in range(n):
                val = rooms[r][c]
                if val == 0:
                    gate_pos.append((r, c, 0))
                    visited_set.add((r, c))

        def get_neighbours(r, c):
            neigbhours = set()
            if 0 <= r + 1 < m and 0 <= c < n and rooms[r + 1][c] == 2147483647:
                neigbhours.add((r + 1, c))
            if 0 <= r - 1 < m and 0 <= c < n and rooms[r - 1][c] == 2147483647:
                neigbhours.add((r - 1, c))
            if 0 <= r < m and 0 <= c + 1 < n and rooms[r][c + 1] == 2147483647:
                neigbhours.add((r, c + 1))
            if 0 <= r < m and 0 <= c - 1 < n and rooms[r][c - 1] == 2147483647:
                neigbhours.add((r, c - 1))
            return neigbhours

        queue = list(gate_pos)
        del gate_pos

        while len(queue) > 0:
            current = queue.pop(0)
            rooms[current[0]][current[1]] = current[2]
            for neigbhour in get_neighbours(current[0], current[1]):
                if (neigbhour[0], neigbhour[1]) not in visited_set:
                    queue.append((neigbhour[0], neigbhour[1], current[2] + 1))
                    visited_set.add((neigbhour[0], neigbhour[1]))
        return rooms


# first get positions of all the gates
# then run a bfs alorith on it with a queue untill the queue is empty
# # also wirte a algo to get neighbours where the value is more that 0
