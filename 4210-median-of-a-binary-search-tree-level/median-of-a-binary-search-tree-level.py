# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelMedian(self, root, level):
        res=[];
        def func(root,l):
            if(root):
                func(root.left,l+1);
                if(l==level):
                    res.append(root.val);
                func(root.right,l+1);
        func(root,0)
        if(res):
            res.sort();
            if(len(res)%2==1):
                return res[len(res)//2];
            else:
                return res[len(res)//2]
        else:
            return -1
        """
        :type root: Optional[TreeNode]
        :type level: int
        :rtype: int
        """
        