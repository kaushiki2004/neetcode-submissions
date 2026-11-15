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
        org = head
        myMap={}
        curr = Node
        
        while org:
            curr = Node(org.val)
            myMap[org] = curr
            org = org.next
        
        org = head
        while org:
            myMap[org].next = myMap.get(org.next)
            myMap[org].random = myMap.get(org.random)
            org = org.next
        return myMap.get(head)