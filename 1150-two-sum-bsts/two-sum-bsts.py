# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        a1=[];
        a2=[];
        res=[0];
        def func1(root):
            if(root):
                func1(root.left);
                a1.append(root.val);
                func1(root.right);
        def func2(root):
            if(root and res[0]==0):
                func2(root.left);
                a2.append(root.val);
                if(target-root.val in a1):
                    res[0]=1;
                    return;
                func2(root.right);
        func1(root1);
        func2(root2);
        for i in a1:
            if(target-i in a2):
                return True;
        return False;
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :type target: int
        :rtype: bool
        """