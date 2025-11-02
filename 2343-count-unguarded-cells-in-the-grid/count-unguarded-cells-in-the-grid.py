class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
        grid=[['0' for i in range(n)]for i in range(m)];
        for [i,j] in walls:
            grid[i][j]='W';
        for [i,j] in guards:
            grid[i][j]='G';
        res=0;
        for [i,j] in guards:
            if(grid[i][j]=='1'):
                res-=1;
            temp=i+1;
            while(temp<m):
                if(grid[temp][j]=='0'):
                    res+=1;
                    grid[temp][j]='1';
                elif(grid[temp][j]=='W' or grid[temp][j]=='G'):
                    break;
                temp+=1;
            temp=i-1;
            while(temp>=0):
                if(grid[temp][j]=='0'):
                    res+=1;
                    grid[temp][j]='1';
                elif(grid[temp][j]=='W' or grid[temp][j]=='G'):
                    break;
                temp-=1;
            temp=j+1;
            while(temp<n):
                if(grid[i][temp]=='0'):
                    res+=1;
                    grid[i][temp]='1';
                elif(grid[i][temp]=='W' or grid[i][temp]=='G'):
                    break;
                temp+=1;
            temp=j-1;
            while(temp>=0):
                if(grid[i][temp]=='0'):
                    res+=1;
                    grid[i][temp]='1';
                elif(grid[i][temp]=='W' or grid[i][temp]=='G'):
                    break;
                temp-=1;

        return m*n-res-len(guards)-len(walls);
        """
        :type m: int
        :type n: int
        :type guards: List[List[int]]
        :type walls: List[List[int]]
        :rtype: int
        """
        