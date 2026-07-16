class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        c = Counter() # Keeps track of character counts in the current window
        left = 0 
        maxLen = 0 # Initialized to store the final result
        
        # number of replacements would be the diff in 
        # frequency of length of curr substring and freq of 
        # most frequent character in the substring. 
        # shrink window when number of replacements > k 
        
        for right in range(len(s)):
            # Add the current character to the window's counter
            c[s[right]] += 1
            
            # Dynamically get the frequency of the most common element in the current window
            most_frequent_count = c.most_common(1)[0][1]
            
            # Calculate current window length
            current_window_len = right - left + 1
            
            # Number of replacements needed is (window length - frequency of most common char)
            numRep = current_window_len - most_frequent_count
            
            # shrink window when number of replacements > k 
            while numRep > k:
                c[s[left]] -= 1 # Remove leftmost character from counter
                left += 1       # Move left pointer up
                
                # Recalculate values for the shrunken window
                most_frequent_count = c.most_common(1)[0][1]
                current_window_len = right - left + 1
                numRep = current_window_len - most_frequent_count
            
            # Update the maximum length found so far
            maxLen = max(right - left + 1, maxLen)

        return maxLen

