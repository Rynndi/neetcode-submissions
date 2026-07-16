class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = set(nums)
        maxLen = 0 
        for num in nums: 

            if (num-1) not in hashmap: 
                #if the left isn't in the hashmap, reset starting point 
                lenCount = 0 
                while (lenCount + num) in hashmap: 
                    lenCount+=1
                maxLen = max(lenCount, maxLen)
            
        return maxLen 
        




        
        