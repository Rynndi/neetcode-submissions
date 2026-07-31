class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastidx = len(nums) - 1 
        farthest = 0 
        j = 0 

        while j <= farthest and j < lastidx: 
            farthest = max(farthest, j + nums[j])
            j+=1 
        if farthest < lastidx: 
            return False
        return True 
        