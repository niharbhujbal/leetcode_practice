class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1
        
        buckets = [0] * (len(nums)+1)
        for key, val in counter.items():
            if buckets[val] ==0:
                buckets[val] = []
            buckets[val].append(key)
        
        count = 0
        ans = []
        for i in buckets[::-1]:
            if i != 0:
                ans.extend(i)
                count += len(i)
            if count >= k:
                break
        
        return ans

