class Solution(object):
    def shiftGrid(self, grid, k):
        m=len(grid);
        n=len(grid[0]);
        for _ in range(k):
            arr=[];
            for i in range(m):
                arr.append(grid[i][n-1])
            arr=arr[-1:]+arr[:-1]
            for i in range(m-1,-1,-1):
                for j in range(n-1,0,-1):
                    grid[i][j]=grid[i][j-1];
            for i in range(m):
                grid[i][0]=arr[i];
        return grid
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        