# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        o=[0];
        def func(root):
            if(root!=None):
                if(root.left==None and root.right==None):
                    return 1;
                left=func(root.left);
                right=func(root.right);
                o[0]=max(o[0],left+right);
                return 1+max(left,right);
            else:
                return 0;
        func(root);
        return o[0];
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        