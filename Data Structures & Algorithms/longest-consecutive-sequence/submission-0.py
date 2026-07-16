class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #running in o(n) time means you cannot sort (nlogn)
        if len(nums) == 0: 
            return 0 

        nums.sort() 

        maxCount = 1
        for i in range(len(nums)): 
            count =1 
            start = nums[i] 
            prev = start 

            for j in range(i+1, len(nums)):
                if nums[j] == prev: 
                    continue 
                elif nums[j] - prev == 1: 
                    prev = nums[j]
                    count+=1 
                else: 
                    break 
            maxCount = max(maxCount, count) 
        return maxCount


            
                

        return maxCount
                 

        
        


        
        