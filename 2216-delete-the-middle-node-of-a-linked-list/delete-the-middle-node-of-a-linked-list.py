# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        n=0;
        temp=head;
        while(temp):
            n+=1;
            temp=temp.next;
        if(n==1):
            return None
        temp=head;
        if(n%2==1):
            n-=1;
        for i in range(n//2-1):
            temp=temp.next;
        temp.next=temp.next.next;
        return head;
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        