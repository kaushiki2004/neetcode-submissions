# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=0
        node=head
        while node:
            count+=1
            node=node.next
        node=head
        if count-n==0:
            return head.next    
        for i in range(count - n-1):
            node=node.next
        node.next = node.next.next
        return head