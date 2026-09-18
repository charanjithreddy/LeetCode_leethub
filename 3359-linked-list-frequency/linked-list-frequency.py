# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def frequenciesOfElements(self, head):
        d={};
        temp=head;
        while(temp):
            if( temp.val in d):
                d[temp.val]+=1;
            else:
                d[temp.val]=1;
            temp=temp.next;
        l=list(d.values());
        newhead=ListNode(l[0]);
        temp=newhead;
        for i in l[1:]:
            new=ListNode(i);
            temp.next=new;
            temp=temp.next;
        return newhead
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        