class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0 
        left = 0 
      
        hashmap = {} 
        #use a map that stores the last index where each char appeared 
        #when character repeats, earliest valid starting point moves to one pos after


        for right in range(len(s)):
            if s[right] in hashmap: 
                #move left to the last index of the seen character 
                left = max(hashmap[s[right]] + 1, left) 
            #update regardless of in the dictionary or not 
            hashmap[s[right]] = right 
            maxLen = max(right - left + 1, maxLen)
        return maxLen

                


        