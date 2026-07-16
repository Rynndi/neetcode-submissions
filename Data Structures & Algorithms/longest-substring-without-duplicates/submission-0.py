class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0 
        left = 0 
        seen = set() 

        for right in range(len(s)):
        
            # if s[right] not in seen: 
            #     seen.add(s[right])
            #     right +=1 
            #     currLen +=1 
            while s[right] in seen: 
                seen.remove(s[left])
                left+=1 
            seen.add(s[right])
            maxLen = max(right - left + 1, maxLen)
        return maxLen

                


        