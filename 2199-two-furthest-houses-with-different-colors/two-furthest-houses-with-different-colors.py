class Solution(object):
    def maxDistance(self, colors):
        n=len(colors)
        res=float("-inf");
        for i in range(n):
            if(colors[i]!=colors[-1]):
                res=max(res,n-i-1);
                break;
        for i in range(n-1,-1,-1):
            if(colors[i]!=colors[0]):
                res=max(res,i);
                break
        return res
        """
        :type colors: List[int]
        :rtype: int
        """