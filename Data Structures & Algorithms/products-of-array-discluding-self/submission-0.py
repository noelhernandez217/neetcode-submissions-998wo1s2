class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)): 
            cp_nums = nums.copy()
            cp_nums.pop(i)
            res = getProd(cp_nums)
            result.append(res)
        return result 
    
def getProd(nums: List[int]) -> int: 
    prod = 1 
    for elem in nums: 
        prod *= elem 
    return prod 
