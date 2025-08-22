class Solution(object):
    def minimumArea(self, grid):
        m=len(grid);
        n=len(grid[0]);
        height_top=m;
        height_bottom=0;
        width_left=n;
        width_right=0;
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1):
                    height_top=min(height_top,i);
                    height_bottom=max(i,height_bottom);
                    width_left=min(width_left,j);
                    width_right=max(width_right,j);
        return (height_bottom-height_top+1)*(width_right-width_left+1);



                    

        """
        :type grid: List[List[int]]
        :rtype: int
        """
        