# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    cnt=0;
    res=-1;
    def kthSmallest(self, root, k):
        cnt=[0];
        res=[-1];
        def func(root):
            if(root and self.res==-1):
                func(root.left);
                self.cnt+=1
                if(self.cnt==k):
                    self.res=root.val;
                    return
                func(root.right);
        func(root)
        return self.res
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        