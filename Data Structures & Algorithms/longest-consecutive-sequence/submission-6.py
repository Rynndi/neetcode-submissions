class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute force approach: SLOW AS BALLS! o(n2 * nlogn)
        #DO NOT SORT!! 
        #the PEAK solution:
        #memory: o(n) (have to remake a set)
        #three distinct sequences: 
        hashmap = set(nums) 
        maxLen = 0 
        for num in nums: 
            #check if it's the start of a sequence 
            #if does not have a left neighbor, starts. 
            if (num-1) not in hashmap: 
                length = 0 
                while (num+length) in hashmap: 
                    length += 1 
                maxLen = max(length, maxLen)
        return maxLen


        
        


        
        