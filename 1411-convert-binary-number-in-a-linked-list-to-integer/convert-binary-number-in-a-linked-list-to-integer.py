# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        temp=head;
        n=0;
        while(temp!=None):
            n+=1;
            temp=temp.next;
        o=0;
        while(head!=None):
            o+=head.val*(2**(n-1));
            n-=1;
            head=head.next;
        return o;

        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        