# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        self.res=True;
        def func(root,l,r):
            if(root!=None):
                if(not l<root.val<r):
                    self.res=False;
                    return;
                func(root.left,l,root.val);
                func(root.right,root.val,r);
            else:
                return;
        func(root,float("-inf"),float("inf"));
        return self.res;
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        