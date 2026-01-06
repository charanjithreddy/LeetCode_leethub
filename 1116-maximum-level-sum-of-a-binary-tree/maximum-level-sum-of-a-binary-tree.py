# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        arr=[root];
        res=[];
        while(len(arr)>0):
            t=[];
            res.append(0);
            for i in arr:
                if(i):
                    res[-1]+=i.val;
                    t.append(i.left);
                    t.append(i.right);
            arr=[i for i in t if i]
        return res.index(max(res))+1;
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """