class Solution(object):
    def areSimilar(self, mat, k):
        m=len(mat);
        n=len(mat[0]);
        k%=n;
        for i in range(m):
            if(i%2==0):
                if(mat[i]!=mat[i][k:]+mat[i][:k]):
                    return False;
            else:
                if(mat[i]!=mat[i][n-k:]+mat[i][:n-k]):
                    return False;
        return True
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: bool
        """