class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        st = [] 

        #i: loop thru currNumrr with idx i 
        #for ea fixed number currNum, we put two pointers
        #left is right after i 
        #right starts at the end 

        for i, currNum in enumerate(nums): 
            #currNum = nums[i]

            #all remaining numbers are positive, won't find 
            if currNum > 0: 
                break
            #skip duplicates 
            if i > 0 and currNum == nums[i-1] :
                continue 
            #two pointers: left = i +1 
            #right = len(nums) - 1 


            left, right = i+1, len(nums) - 1 

            while left < right: 
                threeSum = currNum + nums[left] + nums[right]
                if threeSum > 0: 
                    right -= 1 
                elif threeSum < 0: 
                    left +=1 
                else:
                    st.append([currNum, nums[left], nums[right]])
                    left +=1 
                    right -=1
                    while nums[left] == nums[left - 1] and left < right: 
                        left +=1 

        return st 
