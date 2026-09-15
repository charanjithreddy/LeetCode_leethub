class Solution(object):
    def findBuildings(self, heights):
        res=[];
        h=0;
        for i in range(len(heights)-1,-1,-1):
            if(heights[i]>h):
                res.append(i);
            h=max(h,heights[i])
        return res[::-1]
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        