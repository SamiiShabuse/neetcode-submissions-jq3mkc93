class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        values = {}

        for snum in nums:
            values[snum] = values.get(snum, 0) + 1
        

        return [single_value for single_value, frequency in sorted(values.items(), key = lambda x : x[1], reverse = True)[:k]]