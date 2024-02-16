class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.get_height_length(root)[1]

    def get_height_length(self, root):
        if root is None:
            return 0, 0
        left_height, left_length = self.get_height_length(root.left)
        right_height, right_length = self.get_height_length(root.right)

        return 1 + max(left_height, right_height), max(
            left_height + right_height, left_length, right_length
        )
