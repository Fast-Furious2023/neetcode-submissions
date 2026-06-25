# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        dummy = ListNode()
        prev = dummy

        while l1 or l2:
            if not l1:
                prev.next = l2
                
                break
            if not l2:
                prev.next = l1
                
                break
            if l1.val < l2.val:
                prev.next=l1
                prev = prev.next
                l1=l1.next
            else:
                prev.next=l2
                prev = prev.next
                l2=l2.next
        return dummy.next

            
