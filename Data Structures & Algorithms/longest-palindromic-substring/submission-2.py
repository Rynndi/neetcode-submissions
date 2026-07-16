class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manacher(s): 
            t = "^#" + "#".join(s) + "#$"
            n = len(t) 
            dp = [0] * n 
            left = right = 0 

            for i in range(1, n - 1):
                mirror = left + right - i 

                if i < right:
                    dp[i] = min(right - i, dp[mirror])
                
                while t[i - 1 - dp[i]] == t[i + 1 + dp[i]]:
                    dp[i] += 1 

                if i + dp[i] > right:
                    left = i - dp[i]
                    right = i + dp[i]

            return dp 

        p = manacher(s) 
        resLen, centerIndex = max((v, i) for i, v in enumerate(p))
        resIndex = (centerIndex - resLen) // 2 
        return s[resIndex: resIndex + resLen]