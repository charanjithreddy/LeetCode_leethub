class Solution(object):
    def canPartitionGrid(self, grid):
        m=len(grid);
        n=len(grid[0]);
        r=[0]*m;
        c=[0]*n;
        for i in range(m):
            for j in range(n):
                r[i]+=grid[i][j];
                c[j]+=grid[i][j];
        rowsum=sum(r);
        t=0;
        for i in r:
            t+=i;
            if(t==rowsum-t):
                return True;
        colsum=sum(c);
        t=0;
        for i in c:
            t+=i;
            if(t==colsum-t):
                return True;
        return False
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        