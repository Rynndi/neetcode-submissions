class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sorting handles duplicates easily
        res = set()  # Sets give O(1) lookups instead of O(n)
        
        for i in range(len(nums)):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            seen = set()  # Keeps track of numbers we've checked for this i
            for j in range(i + 1, len(nums)):
                target = -(nums[i] + nums[j])
                
                if target in seen:
                    # Found a triplet! (O(1) add to result set)
                    res.add((nums[i], target, nums[j]))
                
                seen.add(nums[j])
                
        return [list(t) for t in res]
