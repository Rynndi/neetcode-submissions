class Solution:
    def isValid(self, s: str) -> bool:
        st = [] 
        for char in s: 
            if char == '(' or  char == '[' or char == '{':
                st.append(char)
            
            elif char == ')' or char == ']' or char == '}' :
                top = st[-1] if st else False
                if char == ')' and top == '(': 
                    st.pop() 
                elif char == ']' and top == '[':
                    st.pop() 
                elif char == '}' and top == '{':
                    st.pop()
                else: 
                    return False 
            else: 
                continue
       
        if len(st) == 0:
            return True 
        return False
        
      
        


        