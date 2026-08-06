class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[0] = [[]]
        nums = sorted(set(nums))
        for i in range(1, target + 1):
            for cand in nums:
                complement = i - cand 
                if complement <0:
                    continue 
                for combination in dp[complement]:
                    if combination and cand < combination[-1]:
                        continue 
                    dp[i].append(combination + [cand])
        return dp[-1]