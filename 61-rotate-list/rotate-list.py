# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        arr=[]
        n=0
        temp=head;
        while(temp):
            arr.append(temp.val);
            n+=1;
            temp=temp.next;
        if(n==0):
            return head
        k%=n; 
        if(k==0):
            return head  
        arr=arr[n-k:]+arr[:n-k];
        i=0;
        temp=head;
        while(temp):
            temp.val=arr[i];
            i+=1;
            temp=temp.next
        return head
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        