from collections import defaultdict


class Solution:
    def findOrder(self, numCourses, prerequisites):
        hashmap = defaultdict(list)
        for cor in prerequisites:
            hashmap[cor[0]].append(cor[1])
        output = []
        visiting = set()
        visited = set()

        def dfs(cor):
            if cor in visiting:
                return False
            if cor in visited:
                return True

            visiting.add(cor)
            for pre in hashmap[cor]:
                if not dfs(pre):
                    return False
            visiting.remove(cor)
            visited.add(cor)
            output.append(cor)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
