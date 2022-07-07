# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    count = 0
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:   
        self.countSize(head)
        
        size = self.count/2
        while self.count > size:
            self.count -= 1
            head = head.next
        return head    
            
        
    
    def countSize(self, head: Optional[ListNode]):
        self.alreadyCount = True
        if head.next != None:
            self.count += 1
            self.countSize(head.next)
            
        