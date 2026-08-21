# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not (head.next ):
            return 
        
        l=head
        r=head
        while r and r.next:
            l = l.next
            r=r.next.next
        
        curr = l.next
        l.next = None
        
        #reverse
        prev=None
        while curr:
            next= curr.next
            curr.next=prev
            prev = curr
            curr= next
        l=head
        
        r=prev
        while r:
            temp1,temp2 = l.next,r.next
            l.next=r
            r.next=temp1
            l,r=temp1,temp2

