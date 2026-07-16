class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0] 
        
        def robLinear(nums): 
            dp = [0] * (len(nums) + 1) 
            dp[0] = 0 
            dp[1] = nums[0] 
            dpLen = len(dp)

            for i in range(2, dpLen):
                dp[i] = max(dp[i-2] + nums[i-1], dp[i-1])
            return dp[-1]
        
        nums1 = nums[:-1]
        nums2 = nums[1:]
        return max(robLinear(nums1), robLinear(nums2))
        