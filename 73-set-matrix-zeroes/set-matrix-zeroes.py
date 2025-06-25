class Solution(object):
    def setZeroes(self, matrix):
        m=len(matrix);
        n=len(matrix[0]);
        r=set();
        c=set();
        for i in range(m):
            for j in range(n):
                if(matrix[i][j]==0):
                    r.add(i);
                    c.add(j);
        for i in r:
            for j in range(n):
                matrix[i][j]=0;
        for i in range(m):
            for j in c:
                matrix[i][j]=0;
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """