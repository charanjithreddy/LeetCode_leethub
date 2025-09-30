# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.res=0;
        def func(root):
            if(root!=None):
                if(root.left==None and root.right==None):
                    return 1;
                l=func(root.left);
                r=func(root.right);
                self.res=max(self.res,l+r);
                return 1+max(l,r);
            else:
                return 0;
        func(root);
        return self.res;
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """