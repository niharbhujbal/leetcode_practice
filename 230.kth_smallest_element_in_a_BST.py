# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        ans = []

        def kth_smallest_sub(root, present_k, k):
            if root is None or present_k >= k:
                return present_k

            present_k = kth_smallest_sub(root.left, present_k, k)

            present_k += 1
            if present_k == k:
                ans.append(root.val)
            else:
                present_k = kth_smallest_sub(root.right, present_k, k)
            return present_k

        kth_smallest_sub(root, 0, k)
        return ans[0]


# in order traversal produces all the element in ascending order
# so we will store no of node traveled with present k
# when we reach kth node we will append it to ans
# and if the present k is equal or larger than k then we won't go anywhere
