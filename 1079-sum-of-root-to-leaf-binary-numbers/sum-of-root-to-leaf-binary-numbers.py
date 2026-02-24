# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        res=[];
        def func(root,s):
            if(root.left==None and root.right==None):
                s+=str(root.val)
                res.append(s);
                return;
            else:
                s+=str(root.val);
                if(root.left!=None):
                    func(root.left,s);
                if(root.right!=None):
                    func(root.right,s)
            """if(root):
                s+=str(root.val)
                func(root.left,s);
                func(root.right,s);
            else:
                res.append(s);
                return;"""
        func(root,"");
        return sum([int(i,2) for i in res]);
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        