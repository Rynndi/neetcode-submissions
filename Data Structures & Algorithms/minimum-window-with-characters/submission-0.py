class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashmap = defaultdict(int) 
        for char in t:
            hashmap[char] +=1 
 
        ans = "" 
        left = 0 
        missing = len(t) 
        minLen = float("inf")
        
        for right in range(len(s)):
            char = s[right]
            #if this character is needed, satisfy one missing
            if hashmap[char] >0: 
                missing-=1 
            hashmap[char]-=1 

            while missing ==0 :
                if right - left + 1 < minLen: 
                    minLen = right - left + 1 
                    ans = s[left:right + 1]
                leftChar = s[left]
                hashmap[leftChar]+=1 
                if hashmap[leftChar]>0: 
                    missing+=1 
                left +=1 
        return ans
 