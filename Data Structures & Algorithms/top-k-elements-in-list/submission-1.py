class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sortedNums = sorted(counts.keys(), key=counts.get, reverse=True)
        return sortedNums[:k]
           