from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = deque()
        for i in asteroids:
            if len(res) == 0:
                res.append(i)
                continue
            while len(res) != 0 and res[-1] > 0 and i < 0:
                if abs(i) > res[-1]:
                    res.pop()
                elif abs(i) == res[-1]:
                    res.pop()
                    break
                elif abs(i) < res[-1]:
                    break
            else:
                res.append(i)
                

        return list(res)

