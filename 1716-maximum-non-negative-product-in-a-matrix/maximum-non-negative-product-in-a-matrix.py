class Solution(object):
    def maxProductPath(self, grid):
        m=len(grid);
        n=len(grid[0]);
        a=list(grid);
        for i in range(m):
            for j in range(n):
                grid[i][j]=[grid[i][j],grid[i][j]];
        for i in range(m):
            for j in range(n):
                curr=grid[i][j][0];
                t=[];
                if(i-1>=0):
                    t.append(grid[i-1][j][0]*curr);
                    t.append(grid[i-1][j][1]*curr);
                if(j-1>=0):
                    t.append(grid[i][j-1][0]*curr);
                    t.append(grid[i][j-1][1]*curr);
                if(t):
                    grid[i][j][0]=min(t);
                    grid[i][j][1]=max(t);
        if(grid[m-1][n-1][1]>=0):
            return grid[m-1][n-1][1]%(10**9+7)
        else:
            return -1
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        