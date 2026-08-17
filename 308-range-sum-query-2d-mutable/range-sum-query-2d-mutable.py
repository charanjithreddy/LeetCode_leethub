class NumMatrix(object):

    def __init__(self, matrix):
        self.matrix=matrix;
        self.m=len(matrix);
        self.n=len(matrix[0]);
        self.rsum=[];
        for i in range(self.m):
            self.rsum.append([]);
            for j in range(self.n):
                if(j==0):
                    self.rsum[-1].append(matrix[i][j]);
                else:
                    self.rsum[-1].append(self.rsum[-1][-1]+matrix[i][j])
        print(self.rsum)
        """
        :type matrix: List[List[int]]
        """
        

    def update(self, row, col, val):
        self.matrix[row][col]=val;
        self.rsum[row]=[];
        for j in range(self.n):
            if(j==0):
                self.rsum[row].append(self.matrix[row][j]);
            else:
                self.rsum[row].append(self.matrix[row][j]+self.rsum[row][-1])
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: None
        """
        

    def sumRegion(self, row1, col1, row2, col2):
        res=0
        for i in range(row1,row2+1):
            if(col1==0):
                res+=self.rsum[i][col2];
            else:
                res+=self.rsum[i][col2]-self.rsum[i][col1-1]
        return res
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)