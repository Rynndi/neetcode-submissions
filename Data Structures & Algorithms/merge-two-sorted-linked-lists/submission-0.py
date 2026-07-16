# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1 
        curr2 = list2 

        if not curr1:
            return curr2 
        if not curr2:
            return curr1 

        if curr1.val <= curr2.val:
            head = curr1 
            curr1 = curr1.next 
        else: 
            head = curr2 
            curr2 = curr2.next 
        
        ans = head 

        #while both lists are not empty 
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                head.next = curr1
                curr1 = curr1.next 

            else: #curr2.val < curr2.val
                head.next = curr2
                curr2 = curr2.next 
        
            head = head.next 
        #atp, one list is empty 
        if curr1:
            head.next = curr1 
        else: 
            head.next = curr2 
        
        return ans 
        

