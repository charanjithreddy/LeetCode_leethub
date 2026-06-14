# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        res=[];
        while(head):
            res.append(head.val);
            head=head.next;
        n=len(res);
        for i in range(len(res)//2):
            res[i]+=res[n-i-1]
        return max(res)
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        