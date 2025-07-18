# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head=l1;
        curr=head;
        c=0;
        while(l1!=None and l2!=None):
            s=l1.val+l2.val+c;
            l1.val=s%10;
            c=s//10;
            if(l1.next!=None):
                curr=curr.next;
            l1=l1.next;
            l2=l2.next;
        while(l1!=None):
            s=l1.val+c;
            l1.val=s%10;
            c=s//10;
            if(l1.next==None and c>0):
                temp=ListNode(c);
                c=c//10;
                temp.next=None;
                l1.next=temp;
                break;
            l1=l1.next;
        while(l2!=None):
            s=l2.val+c;
            l2.val=s%10;
            c=s//10;
            curr.next=l2;
            curr=curr.next;
            if(l2.next==None and c>0):
                temp=ListNode(c);
                c=c//10;
                temp.next=None;
                curr.next=temp;
                break;
            l2=l2.next;
        if(c>0):
            temp=ListNode(c);
            temp.next=None;
            curr.next=temp;
        return head;
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """