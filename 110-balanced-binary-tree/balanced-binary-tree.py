# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        self.res=True;
        def func(root):
            if(root!=None):
                if(root.left==None and root.right==None):
                    return 1;
                l=func(root.left);
                r=func(root.right);
                if(abs(l-r)>1):
                    self.res=False;
                return 1+max(l,r);
            else:
                return 0;
        func(root);
        return self.res;
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        