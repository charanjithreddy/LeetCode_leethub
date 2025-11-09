class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix);
        n=len(matrix[0]);
        top=0;
        bottom=m-1;
        while(top<=bottom):
            mid1=(top+bottom)//2;
            if(matrix[mid1][0]<=target<=matrix[mid1][-1]):
                l=0;
                r=n-1;
                while(l<=r):
                    mid=(l+r)//2;
                    if(matrix[mid1][mid]==target):
                        return True;
                    elif(matrix[mid1][mid]>target):
                        r=mid-1;
                    else:
                        l=mid+1;  
                break;              
            elif(matrix[mid1][0]>target):
                bottom=mid1-1;
            else:
                top=mid1+1;
        return False;
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        