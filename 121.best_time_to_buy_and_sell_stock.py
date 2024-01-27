class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0
        left = 0
        right = left + 1
        max_profit = 0
        while right <= len(prices) - 1:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
            if prices[left] > prices[right]:
                left = right
                right = left + 1
            else:
                right += 1
        return max_profit


# intialise the pointer at o and 1st index
# we will keep expanding the window until left value is smaller than right value
# if the right value is smaller than left value then shrink window
# bring left pointer there and right pointer again to left+1
# we will keep calculating the max profit and return it at the end
