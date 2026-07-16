class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #brute force approach 
        #take initial array, convert into a set 
        
        #o(n): very efficient. 
        #memory: o(n) (have to remake a set)

        numSet = set(nums) 
        longest = 0 
        for num in nums: 
            #check if it's the start of a sequence 
            #if does not have a left neighbor, starts. 
            if (num-1) not in numSet: 
                length = 0 
                while (num+length) in numSet: 
                    length += 1 
                longest = max(length, longest)
        return longest 


        
        


        
        