# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        a=[];
        def func(root):
            if(root):
                a.append(root.val);
                func(root.left);
                func(root.right);
        func(root);
        return a;
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        