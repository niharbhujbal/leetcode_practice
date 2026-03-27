class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # 5, 10, 20
        five_count = 0
        ten_count = 0
        bills = deque(bills)
        while bills:
            bill = bills.popleft()
            if bill == 5:
                # No change needed; collect and pocket
                five_count += 1

            elif bill == 10:
                # Need exactly $5 change
                if five_count == 0:
                    return False
                five_count -= 1
                ten_count += 1

            else:
                # bill == 20: need $15 change
                # Greedy: prefer $10 + $5 (conserves versatile $5 bills)
                if ten_count >= 1 and five_count >= 1:
                    ten_count -= 1
                    five_count -= 1
                elif five_count >= 3:
                    # Fallback: three $5 bills
                    five_count -= 3
                else:
                    return False
        return True
            
        