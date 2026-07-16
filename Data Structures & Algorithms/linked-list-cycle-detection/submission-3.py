# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        if head is None:
            return False 
        
        curr, faster = head, head 

        while faster and faster.next: 
            curr = curr.next 
            faster = faster.next.next 

            if curr == faster:
                return True 
        
        return False