class Solution(object):
    def maxDepth(self, s):
        res=0;
        curr=0
        for i in s:
            if(i=="("):
                curr+=1;
                res=max(res,curr);
            elif(i==")"):
                curr-=1
        return res
        """
        :type s: str
        :rtype: int
        """
        