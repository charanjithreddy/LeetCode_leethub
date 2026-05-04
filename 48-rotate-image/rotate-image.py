class Solution(object):
    def rotate(self, matrix):
        temp=[];
        n=len(matrix);
        for i in range(n):
            t=[];
            for j in range(n):
                t.append(matrix[j][i]);
            temp.append(t[::-1])
        for i in range(n):
            for j in range(n):
                matrix[i][j]=temp[i][j]

        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        