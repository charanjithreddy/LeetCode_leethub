# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        cnt=[0];
        res=[-1];
        def func(root):
            if(root and res[0]==-1):
                func(root.left);
                cnt[0]+=1
                if(cnt[0]==k):
                    res[0]=root.val;
                    return
                func(root.right);
        func(root)
        return res[0]
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        