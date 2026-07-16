class Solution:
    def findMin(self, nums: List[int]) -> int:
        right =len(nums)-1
        left = 0 
        #the three cases are: 
        #if left < mid > right
            #target is in the right half 
        #if left > mid < right
            #targt is in the left half 
        #if left < mid < right 
            #target is left 
        #cannot have left > mid > right: array is sorted except for that one point 
        if len(nums) == 0:
            return 0 
        if len(nums) == 1:
            return nums[0]

        while left < right: 
            mid = (left + right ) // 2 
            if nums[mid] > nums[right]:
                left = mid + 1 
            else: 
                right = mid 
        return nums[left]
                
