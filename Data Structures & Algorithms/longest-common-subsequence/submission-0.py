class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rowLen, colLen = len(text1), len(text2) 
        dp = [[0 for row in range(colLen + 1)] for col in range(rowLen + 1)]

        for i in range(1, rowLen+1):
            for j in range(1, colLen+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]
        