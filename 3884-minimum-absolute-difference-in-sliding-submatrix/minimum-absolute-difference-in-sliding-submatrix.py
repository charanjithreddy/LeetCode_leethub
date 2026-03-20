class Solution(object):
    def minAbsDiff(self, grid, k):
        res=[];
        m=len(grid);
        n=len(grid[0])
        for i in range(m-k+1):
            res.append([]);
            for j in range(n-k+1):
                t=[];
                for x in range(k):
                    for y in range(k):
                        t.append(grid[i+x][j+y]);
                t=list(set(t));
                if(len(t)<=1):
                    res[-1].append(0);
                else:
                    t.sort()
                    t=[t[z+1]-t[z] for z in range(len(t)-1)];
                    res[-1].append(min(t));
                
                
        return res

        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        