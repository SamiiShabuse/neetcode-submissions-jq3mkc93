class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ''''
            can only do it in 1 pass.
            no storage resturctions
            len max = 1000

            sorting is out of the question
            no binary search not sorted
            
            make a sepearete list build around
            nah its gonna turn itno 

        '''

        hashset = set()

        for val in nums:
            hashset.add(val)

        longest = 0
 
        for val in hashset:
            # only start count if this is beginning of a seq
            if val - 1 not in hashset:
                length = 1

                while val + length in hashset:
                    length += 1

                
                longest = max(longest, length)
                        

        return longest
        