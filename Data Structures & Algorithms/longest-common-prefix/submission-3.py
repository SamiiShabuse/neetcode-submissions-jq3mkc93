class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])): # loop through every idx of first word
            for s in strs: # for every word in the list
                if i == len(s) or s[i] != strs[0][i]: # 
                    return s[:i]
        return strs[0]