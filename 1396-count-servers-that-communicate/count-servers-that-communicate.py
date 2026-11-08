class Solution(object):
    def countServers(self, grid):
        m=len(grid);
        n=len(grid[0]);
        row=[0]*m;
        col=[0]*n;
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    row[i]+=1;
                    col[j]+=1;
        c=0;
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1 and (row[i]>1 or col[j]>1)):
                    c+=1;
        return c;
        """
        :type grid: List[List[int]]
        :rtype: int
        """  