class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        result = []

        for num in nums: 
            if num not in frequency: 
                frequency[num] = 1 
            else: 
                frequency[num] += 1 
        
        for runs in range(k): 
            cur_max = getMax(frequency)
            result.append(cur_max)

        return result

def getMax(frequency: dict[int, int]) -> int: 
    # returns an updated dictionary and the current max 
    max_value = 0
    max_key = None
    for key, value in frequency.items(): 
        if value > max_value: 
            max_value = value 
            max_key = key 

    frequency.pop(max_key) # python does this in place! modifies original
    return max_key

        