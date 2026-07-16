class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counts is a hashmap of number -> frequency 
        #gives you only the unique numbers 
        counts = Counter(nums)
        #counts.keys() sorts, but key = counts.get sorts by frequency
        #like sort(counts.get(number)) 
        #then reverses it 
        sortedNums = sorted(counts.keys(), key=counts.get, reverse=True)
        #return a list, but only of elements up to k 
        return sortedNums[:k]
        #TC: o(nlogn) 