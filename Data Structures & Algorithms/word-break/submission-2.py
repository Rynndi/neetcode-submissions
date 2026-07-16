class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s) 
        dp =[False] * (n+1) 
        dp[0] = True 


        for i in range(1, n+1):
            # for word in wordDict: 
            for j in range(i):
                if dp[j] and s[j:i] in wordDict: 
                # if s[i-len(word):i] == word and dp[i-len(word)]:
                    dp[i] = True 
                    break 
            
        return dp[-1]
        