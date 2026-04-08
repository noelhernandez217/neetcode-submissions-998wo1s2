class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = {}
        for elem in nums: 
            if elem not in tracker: 
                tracker[elem] = 1
            else: 
                tracker[elem] += 1
                return True
        return False
        

        