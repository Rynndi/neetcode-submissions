class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26
        l = 0
        maxf = 0
        for r in range(len(s)):
            idx_r = ord(s[r]) - 65
            count[idx_r] += 1
            if count[idx_r] > maxf:
                maxf = count[idx_r]
            if (r - l + 1) - maxf > k:
                count[ord(s[l]) - 65] -= 1
                l += 1
        return len(s) - l