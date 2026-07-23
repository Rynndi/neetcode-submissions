# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        currNode = head 
        count = 0 

        while count != n and currNode: 
            currNode = currNode.next 
            count+=1 
        
        if currNode is None:
            return head.next 
        
        dummy = head 
        prev = None 
        while currNode: 
            prev = dummy
            dummy = dummy.next 
            currNode = currNode.next 
        
        prev.next = dummy.next 
        return head 