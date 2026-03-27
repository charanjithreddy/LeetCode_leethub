class Solution(object):
    def areSimilar(self, mat, k):
        temp=list(mat);
        m=len(mat);
        n=len(mat[0]);
        k%=n;
        for i in range(m):
            if(i%2==0):
                mat[i]=mat[i][k:]+mat[i][:k];
            else:
                mat[i]=mat[i][n-k:]+mat[i][:n-k];
        return mat==temp
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """
        