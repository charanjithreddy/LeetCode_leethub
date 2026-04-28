class Solution(object):
    def minOperations(self, grid, x):
        t=[];
        r=set();
        for i in grid:
            for j in i:
                t.append(j);
                r.add(j%x);
        if(len(r)>1):
            return -1
        t.sort();
        e=t[len(t)//2];
        res=0;
        for i in t:
            res+=abs(i-e)/x
        return res

        """
        :type grid: List[List[int]]
        :type x: int
        :rtype: int
        """
        