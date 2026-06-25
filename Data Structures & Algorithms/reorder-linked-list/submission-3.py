# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        
        #divide into two halves
        slow=head
        fast=head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        mid = slow


        #reverse the second half
        l=head
        
        curr = mid.next
        mid.next=None
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        r=prev
        #reorder
        while l and r:
            templeft=l.next
            tempright=r.next
            l.next=r
            r.next=templeft
            l = templeft
            r = tempright
        
        
