# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root is None:
            return False
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True
        else:
            left_val = self.isSubtree(root.left, subRoot)
            right_val = self.isSubtree(root.right, subRoot)
        return left_val or right_val

    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False

        return (
            p.val == q.val
            and self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )


# we will check with issame tree function if trees are same are not
# for the sub tree part
# first if the root is none then just return none
# if the root node and subtree node match then run is same algo
# otherwise go ahead and run same algo on left and right of tree
