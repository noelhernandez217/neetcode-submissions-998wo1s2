class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        for i in range(len(strs)): 
            sorted_str = "".join(sorted(strs[i]))
            if sorted_str not in anagram_dict: 
                
                anagram_dict[sorted_str] = [i]
            else: 
                anagram_dict[sorted_str].append(i)

        indices = []
        result = []
        for indices in anagram_dict.values(): 
            temp = []
            for idx in indices: 
                temp.append(strs[idx]) 
            result.append(temp)

        return result