# Definition for Node.
# class Node(object):
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class NodeCopy(object):
    def __init__(self, val=0, left=None, right=None, random=None):
        self.val = val
        self.left = left
        self.right = right
        self.random = random


class Solution(object):
    def copyRandomBinaryTree(self, root):
        d={};
        d[None]=None;
        def func1(root):
            if(root):
                func1(root.left);
                d[root]=NodeCopy(root.val);
                func1(root.right);
        def func2(root):
            if(root):
                func2(root.left);
                d[root].left=d[root.left];
                d[root].right=d[root.right];
                d[root].random=d[root.random]
                func2(root.right);
        func1(root);
        func2(root);
        return d[root];
        """
        :type root: Node
        :rtype: NodeCopy
        """
        