class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        window_size = n - k
        if window_size == 0:                    # must take every card
            return total_sum

        window_sum = sum(cardPoints[:window_size])
        min_window_sum = window_sum
        for i in range(window_size, n):
            # slide right edge to i, drop the element leaving on the left
            window_sum += cardPoints[i] - cardPoints[i - window_size]
            if window_sum < min_window_sum:
                min_window_sum = window_sum
        return total_sum - min_window_sum
            
            

        
