# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if(root!=None):
            if(root.left==None and root.right==None):
                return 1;
            else:
                return 1+max(self.maxDepth(root.left),self.maxDepth(root.right));
        else:
            return 0;
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        