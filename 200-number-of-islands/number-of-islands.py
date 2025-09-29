class Solution(object):
    def numIslands(self, grid):
        res=0;
        m=len(grid);
        n=len(grid[0]);
        mark=[];
        for i in range(m):
            mark.append([0 for j in range(n)]);
        
        def func(r,c):
            mark[r][c]=1;
            if(r+1<m and grid[r+1][c]=='1' and mark[r+1][c]==0):
                func(r+1,c);
            if(c+1<n and grid[r][c+1]=='1' and mark[r][c+1]==0):
                func(r,c+1);
            if(r-1>=0 and grid[r-1][c]=='1' and mark[r-1][c]==0):
                func(r-1,c);
            if(c-1>=0 and grid[r][c-1]=='1' and mark[r][c-1]==0):
                func(r,c-1);
            return;
        for i in range(m):
            for j in range(n):
                if(mark[i][j]==0 and grid[i][j]=='1'):
                    res+=1;
                    func(i,j);
        return res;
        """
        :type grid: List[List[str]]
        :rtype: int
        """