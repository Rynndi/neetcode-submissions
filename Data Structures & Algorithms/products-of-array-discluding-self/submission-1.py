class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # size = len(nums)
        # arr= [None] * size
        # if 0 in nums: 
        #     if nums.count(0)== 1:
        #         #store the index 
        #         zero_index = nums.index(0)
        #         nums.pop(zero_index)
        #         totalProd = math.prod(nums)
        #         arr = [0] * size 
        #         arr[zero_index] = totalProd 
        #         return arr 
    
        #     elif nums.count(0) >1: 
        #         arr = [0] * size 
        #         return arr 

        # totalProd = math.prod(nums)
        # for i in range(len(nums)): 
        #     arr[i] = int(totalProd/nums[i])
        # return arr 

        res = [1] * (len(nums))
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1 
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix 
            postfix *= nums[i] 
        return res 
       
        