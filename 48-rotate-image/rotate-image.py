class Solution(object):
    def rotate(self, matrix):
        a=[];
        n=len(matrix);
        for i in range(n):
            o=[];
            for j in range(n):
                o.append(matrix[j][i]);
            a.append(o[::-1]);
        for i in range(n):
            for j in range(n):
                matrix[i][j]=a[i][j];
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """