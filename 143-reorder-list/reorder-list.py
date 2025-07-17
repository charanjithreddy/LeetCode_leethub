# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        n=0;
        temp1=head;
        while(temp1!=None):
            n+=1;
            temp1=temp1.next;
        if(n!=1):
            temp1=head;
            temp2=head;
            for i in range(n//2):
                if(i==n//2-1):
                    x=temp2.next;
                    temp2.next=None;
                    temp2=x;
                else:
                    temp2=temp2.next;
            prev=None;
            curr=temp2;
            after=None;
            while(curr!=None):
                after=curr.next;
                curr.next=prev;
                prev=curr;
                curr=after;
            temp2=prev;    
            temp=head;
            temp1=temp1.next;
            while(temp1!=None and temp2!=None):
                temp.next=temp2;
                temp=temp.next;
                temp2=temp2.next;

                temp.next=temp1;
                temp=temp.next;
                temp1=temp1.next;
            while(temp2!=None):
                temp.next=temp2
                temp=temp.next;
                temp2=temp2.next;
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """