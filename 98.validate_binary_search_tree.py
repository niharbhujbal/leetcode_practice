class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validate_bst(root, -2e31, 2e31)

    def validate_bst(self, root, range_left, range_right):
        if root is None:
            return True
        return (
            (range_left < root.val < range_right)
            and self.validate_bst(root.left, range_left, root.val)
            and self.validate_bst(root.right, root.val, range_right)
        )


# root value should be between -inf to +inf
# and left child should be (range(left) , root.val)
# right child should be (root.val, range(right))
