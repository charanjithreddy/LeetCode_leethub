class Solution(object):
    def findDiagonalOrder(self, mat):
        i=0;
        j=0;
        m=len(mat);
        n=len(mat[0]);
        o=[];
        x=0;
        while(len(o)<m*n):
            while(i>=0 and j<n):
                o.append(mat[i][j]);
                i-=1;
                j+=1;
                if(i==m and j==n):
                    x=1;
                    break
            i+=1;
            if(j==n):
                j-=1;
                i+=1;
            if(x==1):
                break;
            while(j>=0 and i<m):
                o.append(mat[i][j]);
                i+=1;
                j-=1;
                if(i==m and j==n):
                    x=1;
                    break;
            if(x==1):
                break;
            j+=1;
            if(i==m):
                i-=1;
                j+=1;
        return o;
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        