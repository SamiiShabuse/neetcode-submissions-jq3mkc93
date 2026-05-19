class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        a = {}

        for b in nums:
            a[b] = a.get(b, 0) + 1

        
        return [num for num, freq in sorted(a.items(), key= lambda z: z[1], reverse=True)[:k]]