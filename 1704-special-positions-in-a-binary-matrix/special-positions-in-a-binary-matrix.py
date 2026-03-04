class Solution(object):
    def numSpecial(self, mat):
        m=len(mat);
        n=len(mat[0]);
        rows=[[] for i in range(m)];
        cols=[[] for i in range(n)];
        for i in range(m):
            for j in range(n):
                if(mat[i][j]==1):
                    rows[i].append(i);
                    cols[j].append(j);
        res=0;
        for i in range(m):
            for j in range(n):
                if(mat[i][j]==1 and len(rows[i])==1 and len(cols[j])==1):
                    res+=1;
        return res
        """
        :type mat: List[List[int]]
        :rtype: int
        """