class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        parent_p = {p.val: p}
        parent_q = {q.val: q}

        while p.parent or q.parent:
            # go to p's parent
            if p.parent is not None:
                p = p.parent
                parent_p[p.val] = p

            # got to q's parent
            if q.parent is not None:
                q = q.parent
                parent_q[q.val] = q

            if p.val in parent_q.keys():
                return parent_q[p.val]
            elif q.val in parent_p.keys():
                return parent_p[q.val]


# we will create parent list of both the nodes and store it in hashmap
# run while loop till parent is not node
# and any of the value is present in other list then we will return the answer
