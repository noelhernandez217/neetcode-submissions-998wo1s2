class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_chars = sorted(s)
        t_chars = sorted(t)
        char_dict = {}

        if len(s_chars) != len(t_chars): 
            return False 
        
        for i in range(len(s_chars)): 
            if s_chars[i] != t_chars[i]: 
                return False
        return True