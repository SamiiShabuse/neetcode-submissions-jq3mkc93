class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        word_dict = {} # sorted version : list of actual word

        for s_str in strs:
            sorted_s_str = "".join(sorted(s_str))
            
            if sorted_s_str not in word_dict:
                word_dict[sorted_s_str] = []
            word_dict[sorted_s_str].append(s_str)
        return list(word_dict.values())