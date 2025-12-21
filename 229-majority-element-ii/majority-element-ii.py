class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)
        thrs = len(nums) // 3
        ans = set()
        for i in nums:
            counter[i] += 1
            if counter[i] > thrs and i not in ans:
                ans.add(i)
        
        return list(ans)
        