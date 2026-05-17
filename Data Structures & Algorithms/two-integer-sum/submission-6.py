class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
            given nums, target, return indices of i and j that nums[i] + num[j] == target
            and i != j 

            assum every input has exactly 1 pair of indices.
        '''

        prev = {}

        for i, val in enumerate(nums):
            if (target - val) in prev.keys():
                return [prev[target - val], i]
            prev[val] = i 
        return []
