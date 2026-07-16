class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = Counter() 
        left = 0 
        hashmap = {} 
        maxLen = 0 
        max_freq = 0 # Tracks the highest frequency seen so far in ANY valid window
        
        for right in range(len(s)):
            c[s[right]] += 1
            
            # Maintain the peak frequency. 
            # We don't need to decrease this when left shrinks because a valid 
            # larger window would require an even higher max_freq anyway.
            max_freq = max(max_freq, c[s[right]])
            
            current_window_len = right - left + 1
            numRep = current_window_len - max_freq
            
            # shrink window when number of replacements > k 
            # Changed 'while' to 'if' because the window only expands by 1 per step,
            # so it only ever needs to shrink by at most 1 to become valid again.
            if numRep > k:
                c[s[left]] -= 1 
                left += 1       
                
            maxLen = max(right - left + 1, maxLen)

        return maxLen