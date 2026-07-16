class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # t = "".join(sorted(t))
        # s = "".join(sorted(s))
        # if t == s:
        #     return True 
        # return False 
        if len(s) != len(t):
            return False 

        countS = dict() 
        countT = dict()

        for i in range(len(s)): 
            # if elem doesn't exist in arr already, defaults to 0 
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        return countS == countT 





