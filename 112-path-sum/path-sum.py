# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        self.res=False;
        def func(root,s):
            if(root):
                s+=root.val;
                if(root.left==None and root.right==None):
                    if(s==targetSum):
                        self.res=True;
                    return;
                func(root.left,s);
                func(root.right,s);        
        func(root,0);
        return self.res;
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        