class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict() 
        for i, num in enumerate(nums):
            val = target - num
            
            if val in hashmap:
                return [hashmap[val], i]
            hashmap[num] = i
            





