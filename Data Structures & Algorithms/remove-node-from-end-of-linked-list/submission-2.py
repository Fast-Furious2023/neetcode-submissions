# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #fast pointer move (n-1) steps ahead before slow pointer
        
        slow=head
        fast=head
        for _ in range(n):
            fast=fast.next
        if not fast:
            return head.next
        prev=None
        while fast:
            prev=slow
            slow=slow.next
            fast=fast.next

        target=slow
        temp = target.next
        prev.next=temp
        return head
