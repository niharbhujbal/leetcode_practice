class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rotten_oranges_pos = []
        total_oranges = 0
        visited_set = set()
        for r in range(m):
            for c in range(n):
                val = grid[r][c]
                if val == 2:
                    rotten_oranges_pos.append((r, c, 0))
                    visited_set.add((r, c))
                if val != 0:
                    total_oranges += 1
        if total_oranges == 0:
            return 0

        def get_neighbours(r, c):
            neigbhours = set()
            if 0 <= r + 1 < m and 0 <= c < n and grid[r + 1][c] == 1:
                neigbhours.add((r + 1, c))
            if 0 <= r - 1 < m and 0 <= c < n and grid[r - 1][c] == 1:
                neigbhours.add((r - 1, c))
            if 0 <= r < m and 0 <= c + 1 < n and grid[r][c + 1] == 1:
                neigbhours.add((r, c + 1))
            if 0 <= r < m and 0 <= c - 1 < n and grid[r][c - 1] == 1:
                neigbhours.add((r, c - 1))
            return neigbhours

        queue = list(rotten_oranges_pos)
        # visited_set = set(queue)
        while len(queue) > 0:
            current = queue.pop(0)
            grid[current[0]][current[1]] = 2
            # visited_set.add((current[0], current[1]))
            for neigbhour in get_neighbours(current[0], current[1]):
                if (neigbhour[0], neigbhour[1]) not in visited_set:
                    queue.append((neigbhour[0], neigbhour[1], current[2] + 1))
                    visited_set.add((neigbhour[0], neigbhour[1]))
        if len(visited_set) == total_oranges:
            return current[2]
        else:
            return -1


# first we have to find all the orange r,c where they are rotten, we will also count total no of oranges
# then run a loop of over this oranges where it will run a bfs algorithm
# create a queue in from which we will do all the operation
# bfs algorithm will run while the queue is all empty
# first queue will have rotten oranges and will go to that orange then change the value and add all the neighbours to the queue with a called minute
# track visited too
# increment to no with r,c +1 and add it to queue
