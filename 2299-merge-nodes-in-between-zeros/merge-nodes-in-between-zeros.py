# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        temp=head;
        it=head.next;
        t=0;
        while(it):
            if(it.val==0):
                temp.val=t;
                t=0;
                if(it.next):    
                    temp=temp.next;
                else:
                    temp.next=None;
            else:
                t+=it.val;
            it=it.next;

        return head

        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        