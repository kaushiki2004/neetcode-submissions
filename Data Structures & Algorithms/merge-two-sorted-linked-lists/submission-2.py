class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=list1
        l2=list2
        node=None
        head=None
        if not l1 and not l2:
            return None
        elif not l1 and l2:
            head = l2
            l2=l2.next
        elif l1 and not l2:
            head = l1
            l1=l1.next
        else:
            if l1.val<=l2.val:
                head=l1
                l1=l1.next
            else:
                head=l2
                l2=l2.next

        node=head
        if not head:
            return None
        while l1 or l2:
            if not l1:
                node.next = l2
                break
            elif not l2:
                node.next = l1
                break
            else:
                if l1.val<=l2.val:
                    node.next=l1
                    l1=l1.next
                    node=node.next
                else:
                    node.next=l2
                    l2=l2.next
                    node=node.next

            
        return head