# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        def reverse(root):
            if(root!=None):
                root.left,root.right=root.right,root.left;

        def func(root):
            if(root!=None):
                reverse(root);
                func(root.left);
                func(root.right);

        if(root!=None):
            func(root);
        return root;

        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        