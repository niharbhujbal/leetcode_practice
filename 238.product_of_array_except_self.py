class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_product = []
        for i, j in enumerate(nums):
            if i == 0:
                product = j
            else:
                product *= j
            left_product.append(product)

        right_product = []
        for i, j in enumerate(nums[::-1]):
            if i == 0:
                product = j
            else:
                product *= j
            right_product = [product] + right_product

        ans = []
        for i in range(len(nums)):
            if i == 0:
                ans.append(right_product[1])
            elif i == len(nums) - 1:
                ans.append(left_product[-2])
            else:
                ans.append(left_product[i - 1] * right_product[i + 1])

        return ans


# create a array of product of all the left element for a given index
# create a array of product of all the right elements of a given index
# at the merge them
