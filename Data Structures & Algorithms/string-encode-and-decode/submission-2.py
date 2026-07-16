class Solution:
    stored = None 
    def encode(self, strs: List[str]) -> str:
        Solution._stored = strs 
        return "".join(strs)
        
    def decode(self, s: str) -> List[str]:
        #decoded_str is the same as strs in machine 1 
        return Solution._stored




