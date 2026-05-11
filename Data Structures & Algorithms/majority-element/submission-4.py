class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
            can you solve with linear time and O(1) space?

            O(1) space storing a constant, linear means we just do 1-pass
        '''

        res = cnt = 0

        for num in nums:
            if cnt == 0:
                res = num

            cnt += (1 if num == res else -1)
        return res

