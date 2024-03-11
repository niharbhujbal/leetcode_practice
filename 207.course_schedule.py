from collections import defaultdict


class Solution:
    def canFinish(self, numCourses, prerequisites):
        hashmap = defaultdict(list)
        for cor in prerequisites:
            hashmap[cor[0]].append(cor[1])
        visiting = set()

        def dfs(cor):
            if cor in visiting:
                return False
            if hashmap[cor] == []:
                return True

            visiting.add(cor)
            for pre in hashmap[cor]:
                if not dfs(pre):
                    return False
            visiting.remove(cor)
            hashmap[cor] = []
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
