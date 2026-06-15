# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        slow=head;
        fast=head.next;
        while(fast and fast.next and fast.next.next):
            slow=slow.next;
            fast=fast.next.next;
        if(not slow.next):
            return None
        slow.next=slow.next.next;
        return head
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        