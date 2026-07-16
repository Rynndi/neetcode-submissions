class Solution:
    def longestPalindrome(self, s: str) -> str:
        def manacher(s): 
            t = "^#" + "#".join(s) + "#$"
            n = len(t) 
            dp = [0] * n 

            #store boundaries of the current rightmost palindrome 
            #t[left: right+1] is the palindrome that currently reaches farthest to the right 

            left = right = 0 

            for i in range(1, n - 1):
                #center is (left + right // 2), mirror = 2 * center - i 
                #find the index on the opposite side of the current palindrome 
                mirror = left + right - i 
                #if i is inside the known palindrome, mirror already processed. reuse dp[mirror] 
                if i < right:
                    #if i inside the curr rightmost palindrome, initialize dp using its mirror 
                    #if the mirror palindrome fits perfectly inside, copy it directly dp[i] = dp[mirror]
                    #if the mirror palindrome goes past right, cannot trust the whole mirror. Go to boundary 
                    dp[i] = min(right - i, dp[mirror])
                
                #expand normally. Check if the palindrome can still grow (center expansion) 
                #sentinels make it safe because eventually one side hits ^ or $, and then cannot match 
                while t[i - 1 - dp[i]] == t[i + 1 + dp[i]]:
                    dp[i] += 1 

                #if palindrome centered at i reaches farther right than anything before it, make it the new current rightmost palindrome 
                
                if i + dp[i] > right:
                    left = i - dp[i]
                    right = i + dp[i]

            return dp 

        p = manacher(s) 

        resLen, centerIndex = max((v, i) for i, v in enumerate(p))
        resIndex = (centerIndex - resLen) // 2 
        return s[resIndex: resIndex + resLen]