class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        st = [] 

        for word in strs: 
            hashmap["".join(sorted(word))].append(word)
        
        #returns only the first group. 
        for value in hashmap.values(): 
            st.append(value)
        return st
            
        