# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        self.res=False;
        def same(root,subRoot):
            if(root==None and subRoot==None):
                return True;
            elif(root==None or subRoot==None):
                return False;
            else:
                if(root.val!=subRoot.val):
                    return False;
                else:
                    return same(root.left,subRoot.left) and same(root.right,subRoot.right);

        def inorder(root):
            if(root!=None):
                inorder(root.left);
                if(root.val==subRoot.val):
                    if(same(root,subRoot)):
                        self.res=True;
                inorder(root.right);
        inorder(root);
        return self.res;
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        