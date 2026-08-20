# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        p1,p2=dummy,head
        count=0
        while p2:
            if count==n:
                p1=p1.next
            else:
                count+=1
            p2=p2.next
        p1.next = p1.next.next  
        return dummy.next      