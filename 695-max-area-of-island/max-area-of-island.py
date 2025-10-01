class Solution(object):
    def maxAreaOfIsland(self, grid):
        res=[0];
        m=len(grid);
        n=len(grid[0]);
        visited=[[0 for i in range(n)]for i in range(m)];
        def func(i,j):
            visited[i][j]=1;
            if(i+1<m and grid[i+1][j]==1 and visited[i+1][j]==0):
                res[-1]+=1;
                func(i+1,j);
            if(j+1<n and grid[i][j+1]==1 and visited[i][j+1]==0):
                res[-1]+=1;
                func(i,j+1);
            if(i-1>=0 and grid[i-1][j]==1 and visited[i-1][j]==0):
                res[-1]+=1;
                func(i-1,j);
            if(j-1>=0 and grid[i][j-1]==1 and visited[i][j-1]==0):
                res[-1]+=1;
                func(i,j-1);
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1 and visited[i][j]==0):
                    res.append(1);
                    func(i,j);
        return max(res);
        """
        :type grid: List[List[int]]
        :rtype: int
        """