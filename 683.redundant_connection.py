class Solution:
    def findRedundantConnection(self, edges):

        reperentative = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            p = reperentative[n]
            while p != reperentative[p]:
                p = reperentative[p]

            return p

        def union(a, b):
            ap = find(a)
            bp = find(b)
            if ap == bp:
                return False

            if rank[ap] > rank[bp]:
                reperentative[bp] = ap
                rank[ap] = rank[ap] + rank[bp]
            else:
                reperentative[ap] = bp
                rank[bp] = rank[ap] + rank[bp]
            return True

        for ele1, ele2 in edges:
            if not union(ele1, ele2):
                return [ele1, ele2]
