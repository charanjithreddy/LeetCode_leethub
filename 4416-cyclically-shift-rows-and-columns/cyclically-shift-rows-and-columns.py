class Solution(object):
    def cyclicShift(self, n, grid, rowShift, colShift):
        for i in range(n):
            grid[i]=grid[i][rowShift[i]:]+grid[i][:rowShift[i]]
        for i in range(n):
            t=[];
            for j in range(n):
                t.append(grid[j][i]);
            t=t[colShift[i]:]+t[:colShift[i]];
            for j in range(n):
                grid[j][i]=t[j]
        return grid
        """
        :type n: int
        :type grid: List[List[int]]
        :type rowShift: List[int]
        :type colShift: List[int]
        :rtype: List[List[int]]
        """
        