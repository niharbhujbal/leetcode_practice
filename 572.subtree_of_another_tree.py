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
        if (
            self.isSameTree(root.left, subRoot)
            or self.isSameTree(root.right, subRoot)
            or self.isSameTree(root, subRoot)
        ):
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
