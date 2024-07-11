class Solution(object):
    def diagonalSum(self, mat):
        sum=0;
        l=len(mat);
        for i in range(l):
            for j in range(l):
                if (i==j or i+j==l-1):
                    sum+=mat[i][j];

        return sum;

        """
        :type mat: List[List[int]]
        :rtype: int
        """
        