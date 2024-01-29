class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.kth_smallest(root, [], k)[-1]

    def kth_smallest(self, root, traversed_list, k):
        if root is None or len(traversed_list) == k:
            return traversed_list

        traversed_list = self.kth_smallest(root.left, traversed_list, k)
        if len(traversed_list) < k:
            traversed_list.append(root.val)
        traversed_list = self.kth_smallest(root.right, traversed_list, k)
        return traversed_list


# in order traversal produces all the element in ascending order
# so while traversing keep track of k and when k is 0 the return that number
# if the root value is None the retun none and k value
# if if k value is not 0 then call same function for left child and recieve
