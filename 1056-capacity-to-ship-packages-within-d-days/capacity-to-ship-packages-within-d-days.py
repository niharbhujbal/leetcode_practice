class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # capcity low to high
        # more days to less days
        # 
        # calculate days required based on capacity
        def calculate_days(capacity):
            days = 1
            cargo = 0
            for i in weights:
                if cargo + i <= capacity:
                    cargo += i
                else:
                    days += 1
                    cargo = i
            return days
        
        left = max(weights)
        right = sum(weights)

        ans = -1
        while left <= right:
            mid = left + (right - left) // 2
            days_required = calculate_days(mid)
            if days_required <= days:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return int(ans)