# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        n=0;
        temp=head;
        while(temp!=None):
            temp=temp.next;
            n+=1;
        if(n!=1):
            temp=head;
            temp1=head;
            x=None;
            for i in range(n//2):
                if(i==n//2-1):
                    x=temp1;
                temp1=temp1.next;
            x.next=None;
            prev=None;
            curr=temp1;
            after=None;
            while(curr!=None):
                after=curr.next;
                curr.next=prev;
                prev=curr;
                curr=after;
            temp1=prev;
            pointer=head;
            temp=temp.next;
            while(temp!=None and temp1!=None):
                pointer.next=temp1;
                pointer=pointer.next;
                temp1=temp1.next;
                pointer.next=temp;
                pointer=pointer.next;
                temp=temp.next;
            pointer.next=temp1;
            pointer=pointer.next;
            temp1=temp1.next;
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        