# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        res=[];
        queue=[root];
        while(queue):
            t=[];
            for i in range(len(queue)):
                temp=queue.pop(0);
                if(temp):
                    t.append(temp.val);
                    queue.append(temp.left);
                    queue.append(temp.right);
            if(t):
                res.append(t);
        return res;
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """