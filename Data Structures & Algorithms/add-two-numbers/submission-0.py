# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #read the two numbers

        def listToNumber(self, li):
            curr = li
            number1=0
            i = 0
            while curr:
              number1 += curr.val*(10**i)
              i += 1
              curr = curr.next
            return number1
        
        n1=listToNumber(self, l1)
        n2=listToNumber(self, l2)

        #calcuate the sum
        sum = n1 + n2
        #turn the sum into a linked list
        res = str(sum)[::-1]
        head = ListNode(int(res[0]))
        curr = head
        for i in range(len(res)):
            curr.next = ListNode(int(res[i+1])) if i < len(res)-1 else None
            curr=curr.next
        return head
