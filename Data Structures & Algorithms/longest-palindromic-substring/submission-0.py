class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Instead of checking the same substring over and over again, 
        #remember whether substring is a palindrome 

        #substring is a palindrome when the end characters match, and inside is also a palindrome. 
        #oh, i get it. It's a truth table. 


        #dp[i][j] is true if s[i..j] is a palindrome. 
        #s[i..j] is a palindrome when s[i] == s[j]
        #inside is also a palindrome: dp[i+1][j-1]
        resIdx, resLen = 0, 0
        n = len(s) 
        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <=2 or dp[i+1][j-1]):
                    dp[i][j] = True 
                    if resLen < (j - i + 1):
                        resIdx = i 
                        resLen = j - i + 1 
        return s[resIdx: resIdx + resLen]