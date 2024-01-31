# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total_sum = 0

        def dfs(node, path):
            nonlocal total_sum
            if node is None:
                total_sum += int(path)
                return None

            path += str(node.val)
            if node.right is None:
                dfs(node.left, path)
            elif node.left is None:
                dfs(node.right, path)
            else:
                dfs(node.left, path)
                dfs(node.right, path)

        dfs(root, "")
        return total_sum


# create a paths list
# depth first search algorithm with path as input pre ore order
# terminating condition
# if node is none just upload the path to paths by converting it into no's
# else cal the dfs of add current node value to path
# the call dfs on left and right node
# here we have three conditions if the node has both child as none then it is end
# if just left node is node then we should only call dfs on right as it is not end of the path and vice versa
# at end just return sum
