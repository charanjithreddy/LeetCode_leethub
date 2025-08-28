class Solution(object):
    def sortMatrix(self, grid):
        o=[];
        n=len(grid);
        for i in range(len(grid)-1,0,-1):
            t=i;
            j=0;
            temp=[];
            while(t<len(grid)):
                temp.append(grid[j][t]);
                j+=1;
                t+=1;
            temp.sort();
            o.append(temp);
        
        for i in range(len(grid)):
            t=i;
            j=0;
            temp=[];
            while(t<len(grid)):
                temp.append(grid[t][j]);
                j+=1;
                t+=1;
            temp.sort(reverse=True);
            o.append(temp);
        arr=[];
        for i in o:
            for j in i:
                arr.append(j);
        ind=0;
        for i in range(len(grid)-1,0,-1):
            t=i;
            j=0;
            temp=[];
            while(t<len(grid)):
                grid[j][t]=arr[ind]
                j+=1;
                t+=1;
                ind+=1;
        for i in range(len(grid)):
            t=i;
            j=0;
            temp=[];
            while(t<len(grid)):
                grid[t][j]=arr[ind]
                j+=1;
                t+=1;
                ind+=1;
        return grid;
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        