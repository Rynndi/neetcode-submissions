class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join([char.lower() for char in s if char.isalnum()])
        i = 0 
        j = len(s1) - 1 
        while i < j: 
            if s1[i] != s1[j]: 
                return False 
            i+=1 
            j-=1 
        return True 
        
