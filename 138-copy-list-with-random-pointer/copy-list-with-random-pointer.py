"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        t={};
        t[None]=None;
        temp=head;
        while(temp!=None):
            new=Node(temp.val);
            t[temp]=new;
            temp=temp.next;
        temp=head;
        while(temp!=None):
            t[temp].next=t[temp.next];
            t[temp].random=t[temp.random];
            temp=temp.next;
        return t[head];
        """
        :type head: Node
        :rtype: Node
        """