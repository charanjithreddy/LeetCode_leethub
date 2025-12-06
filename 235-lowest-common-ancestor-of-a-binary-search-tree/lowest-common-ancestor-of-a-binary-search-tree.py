# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        p,q=min(p.val,q.val),max(p.val,q.val);
        while(root):
            if(root.val>=p and root.val<=q):
                return root;
            elif(root.val>p and root.val>q):
                root=root.left;
            else:
                root=root.right;
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        