class Solution(object):
    def reverseSubmatrix(self, grid, x, y, k):
        t=[];
        for i in range(k):
            temp=[];
            for j in range(k):
                temp.append(grid[x+i][y+j]);
            t.append(temp);
        t=t[::-1];
        for i in range(k):
            for j in range(k):
                grid[x+i][y+j]=t[i][j]
        return grid
        """
        :type grid: List[List[int]]
        :type x: int
        :type y: int
        :type k: int
        :rtype: List[List[int]]
        """