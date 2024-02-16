class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.calculate_height_of_node(root)[0]

    def calculate_height_of_node(self, root):
        if root is None:
            return True, -1

        if root.left is not None:
            is_balanced_left, left_height = self.calculate_height_of_node(root.left)
        else:
            is_balanced_left, left_height = True, 0

        if root.right is not None:
            is_balanced_right, right_height = self.calculate_height_of_node(root.right)
        else:
            is_balanced_right, right_height = True, 0

        return (
            abs(left_height - right_height) <= 1
            and is_balanced_right
            and is_balanced_left,
            1 + max(left_height, right_height),
        )


# a new fuction to calculate the height of tree
# here we want to solve problem recursively
# we want to calculate the height of each node on left and right
# so this function will return height of left right and if the difference between heights is more than 1
# this new function will check
