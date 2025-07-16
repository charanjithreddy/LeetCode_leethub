# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def hasCycle(self, head):
        temp=head;
        while(temp!=None and temp.next!=None):
            
            head=head.next;
            temp=temp.next.next;
            if(head==temp):
                return True;
        return False;
        """
        :type head: ListNode
        :rtype: bool
        """