class Solution(object):
    def countCoveredBuildings(self, n, buildings):
        rows=[[float('inf'),float('-inf')] for i in range(n+1)];
        cols=[[float('inf'),float('-inf')] for i in range(n+1)];
        for i in buildings:
            rows[i[0]][0]=min(i[1],rows[i[0]][0]);
            rows[i[0]][1]=max(i[1],rows[i[0]][1]);

            cols[i[1]][0]=min(i[0],cols[i[1]][0]);
            cols[i[1]][1]=max(i[0],cols[i[1]][1]);
        res=0;
        for i in buildings:
            if(rows[i[0]][0]<i[1]<rows[i[0]][1] and cols[i[1]][0]<i[0]<cols[i[1]][1]):
                res+=1;
        return res;
        """
        :type n: int
        :type buildings: List[List[int]]
        :rtype: int
        """
        