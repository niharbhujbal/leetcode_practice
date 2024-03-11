class Solution:
    def countComponents(self, n, edges):
        reperentative = [i for i in range(n)]
        rank = [1] * (n)

        def find(n):
            p = reperentative[n]
            while p != reperentative[p]:
                p = reperentative[p]

            return p

        def union(a, b):
            ap = find(a)
            bp = find(b)

            if rank[ap] > rank[bp]:
                reperentative[bp] = ap
                rank[ap] = rank[ap] + rank[bp]
            else:
                reperentative[ap] = bp
                rank[bp] = rank[ap] + rank[bp]

        for ele1, ele2 in edges:
            union(ele1, ele2)
        total_groups = set()
        for i in range(n):
            total_groups.add(find(i))
        return len(total_groups)
