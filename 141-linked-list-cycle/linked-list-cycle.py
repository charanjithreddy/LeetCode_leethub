# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def hasCycle(self, head):
        temp1=head;
        if(temp1==None):
            return False;
        temp2=head.next;
        while(temp2!=None and temp2.next!=None):
            if(temp1==temp2):
                return True;
            temp1=temp1.next;
            temp2=temp2.next.next;
        return False;
        """
        :type head: ListNode
        :rtype: bool
        """