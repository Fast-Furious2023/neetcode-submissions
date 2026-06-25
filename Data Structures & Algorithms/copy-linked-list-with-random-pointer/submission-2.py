"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        new = {}
        curr = head
        i = 0
        while curr:
            new[curr]= [i, Node(curr.val)]
            i += 1
            curr = curr.next
        
        for node, [index,newNode] in new.items():
            newNode.next=    new[node.next][1] if node.next else None
            if node.random is None:
                newNode.random = None 
            else:
                newNode.random =    new[node.random][1]
        
        return    new[head][1]
