class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #kadane's algorithm: 
        #stores max found so far 
        res = nums[0] 
        maxEnding = nums[0] 
       
        #multiplication is annoying because two negatives can make a positive
        minEnding = nums[0] 
        for i in range(1, len(nums)):
            tmp = maxEnding * nums[i]
            maxEnding = max(maxEnding * nums[i], minEnding * nums[i], nums[i])
            minEnding = min(tmp, minEnding * nums[i], nums[i])
            res = max(res, maxEnding)
        return res 


        