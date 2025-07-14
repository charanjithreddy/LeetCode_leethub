class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix);
        n=len(matrix[0]);
        top=0;
        bottom=m-1;
        while(top<=bottom):
            mid=(top+bottom)//2;
            if(matrix[mid][0]<=target):
                left=0;
                right=n-1;
                while(left<=right):
                    col=(left+right)//2;
                    if(matrix[mid][col]==target):
                        return True;
                    elif(matrix[mid][col]<target):
                        left=col+1;
                    else:
                        right=col-1;
                top=mid+1;            
            else:
                bottom=mid-1;
        return False;
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        