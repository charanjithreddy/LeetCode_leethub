# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        def func(root,max_val):
            if(root==None):
                return 0;
            res=0;
            if(root.val>=max_val):
                res=1;
            max_val=max(max_val,root.val);
            return res+func(root.left,max_val)+func(root.right,max_val);
        return func(root,root.val)
        """
        :type root: TreeNode
        :rtype: int
        """
        