class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #two pointers: 
        left = 0 
        right = 1 
        maxP = 0 

        while right < len(prices): 
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = right 
            right += 1
        return maxP 

        