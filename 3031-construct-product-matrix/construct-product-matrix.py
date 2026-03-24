class Solution(object):
    def constructProductMatrix(self, grid):
        m=len(grid);
        n=len(grid[0]);
        p=[];
        for i in grid:
            for j in i:
                p.append(j);
        lr=list(p);
        for i in range(1,len(lr)):
            lr[i]*=lr[i-1]%12345;
        rl=list(p);
        for i in range(len(rl)-2,-1,-1):
            rl[i]*=rl[i+1]%12345;
        res=[rl[1]];
        res.extend([lr[i-1]*rl[i+1] for i in range(1,len(lr)-1)]);
        res.append(lr[-2]);
        ind=0;
        for i in range(m):
            for j in range(n):
                grid[i][j]=res[ind]%12345;
                ind+=1
        return grid
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """