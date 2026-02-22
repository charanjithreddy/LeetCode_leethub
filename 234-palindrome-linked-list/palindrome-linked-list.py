# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        n=0;
        temp=head;
        while(temp):
            n+=1;
            temp=temp.next;
        stack=[];
        temp=head;
        for i in range(n//2):
            stack.append(temp.val);
            temp=temp.next;
        if(n%2==1):
            temp=temp.next;
        for i in range(n//2):
            if(temp.val!=stack[-1]):
                return False;
            else:
                temp=temp.next;
                stack.pop(-1);
        return True
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """