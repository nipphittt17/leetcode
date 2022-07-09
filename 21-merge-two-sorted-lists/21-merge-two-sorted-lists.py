# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    output = []
    count = 0
    
    def list_to_link(self, lst):
        """Takes a Python list and returns a Link with the same elements.
        """
        if len(lst) == 1:
            return ListNode(lst[0])
        return ListNode(lst[0], self.list_to_link(lst[1:])) 
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if self.count == 0:
            self.output = []
            self.count += 1
        if list1 == None and list2 == None:
            return list1
        if list1 == None:
            self.output.append(list2.val)
            if list2.next != None:
                self.mergeTwoLists(list1,list2.next)
        elif list2 == None:
            self.output.append(list1.val)
            if list1.next != None:
                self.mergeTwoLists(list1.next,list2)     
        else:
            if list1.val < list2.val :
                self.output.append(list1.val)
                print(self.output)     
                self.mergeTwoLists(list1.next,list2)
            else:
                self.output.append(list2.val)
                print(self.output)
                self.mergeTwoLists(list1,list2.next)
            
        return self.list_to_link(self.output)