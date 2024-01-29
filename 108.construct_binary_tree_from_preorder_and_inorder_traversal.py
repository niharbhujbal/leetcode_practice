# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        indexes = {}
        for ind, val in enumerate(inorder):
            indexes[val] = ind

        return self.construct_root(0, len(preorder), inorder, indexes, preorder, -1)[0]

    def construct_root(self, left, right, indexes, preorder, pointer):
        if left >= right:
            return None, pointer
        pointer += 1
        root = TreeNode(preorder[pointer])
        index_ = indexes[preorder[pointer]]
        root.left, pointer = self.construct_root(
            left, index_, indexes, preorder, pointer
        )
        root.right, pointer = self.construct_root(
            index_ + 1, right, indexes, preorder, pointer
        )
        return root, pointer
