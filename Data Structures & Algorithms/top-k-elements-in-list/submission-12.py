class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        vals = {}

        for num in nums:
            vals[num] = vals.get(num, 0) + 1
        
        return [num for num, freq in sorted(vals.items(), key=lambda x: x[1], reverse=True)[:k]]