class Solution(object):
    def maxDistance(self, colors):
        d={};
        for i in range(len(colors)):
            if(colors[i] in d):
                d[colors[i]].append(i);
            else:
                d[colors[i]]=[i];
        res=float("-inf");
        for i in d:
            for j in d:
                if(i!=j):
                    res=max(res,max(d[i])-min(d[j]),max(d[j])-min(d[i]));
        return res
        """
        :type colors: List[int]
        :rtype: int
        """
        