# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def hasCycle(self, head):
        s=set();
        while(head!=None):
            if(head in s):
                return True;
            else:
                s.add(head);
            head=head.next;
        return False;
        """
        :type head: ListNode
        :rtype: bool
        """