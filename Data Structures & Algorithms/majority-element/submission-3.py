class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
            array nums of size n,
                return most popular element
                
            popular elemnts = appears more than 1/2 times in array
            assume always in array
        '''

        # approach 1 with a hashmap

        number = defaultdict(int)

        for num in nums:
            number[num] += 1

        return max(number, key=number.get)