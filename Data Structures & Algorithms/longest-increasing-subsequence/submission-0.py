class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums) 
        dp = [1] * (n)


        #dp[i] = len of longest subsequence up to i 
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]: 
                    dp[i] = max(dp[j]+1, dp[i]) 

        print(dp)
        return max(dp)

