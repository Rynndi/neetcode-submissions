class Solution:
    def maxArea(self, heights: List[int]) -> int:
        totMax = -69696969696969 
        left = 0 
        right = len(heights) - 1 
        while left < right: 
            rHeight = heights[right]
            lHeight = heights[left]
            currVol= min(lHeight, rHeight) * (right - left) 
            totMax = max(currVol, totMax)
            #move the pointer to the shorter of the two walls 
            if rHeight > lHeight: 
                left+=1 
            elif rHeight < lHeight:
                right-=1 
            else: 
                right-=1
        return totMax

                



        