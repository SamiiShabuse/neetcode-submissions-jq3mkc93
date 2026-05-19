class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        ret = {}

        for num in nums:
            ret[num] = ret.get(num, 0) + 1
        
        return [num for num, freq in sorted(ret.items(), key=lambda x : x[1], reverse=True)[:k]]