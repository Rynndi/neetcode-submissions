class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        maxEnding = nums[0]

        for i in range(1, len(nums)):
            maxEnding = max(maxEnding + nums[i], nums[i])
            ans = max(ans, maxEnding)
        return ans 
        