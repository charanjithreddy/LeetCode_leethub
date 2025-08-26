class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        res_d=2;
        res_a=1;
        for [l,w] in dimensions:
            if(l*l+w*w>res_d):
                res_d=l*l+w*w;
                res_a=l*w;
            elif(l*l+w*w==res_d):
                res_a=max(res_a,l*w);
        return res_a;
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """