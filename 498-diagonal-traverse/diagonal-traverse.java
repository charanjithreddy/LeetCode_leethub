class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int i=0,j=0;
        int m=mat.length,n=mat[0].length;
        int res[]=new int[m*n];
        int ind=0;
        while(ind<m*n){
            while(i>=0 && j<n){
                res[ind++]=mat[i][j];
                i-=1;
                j+=1;
            }
            i+=1;
            if(j==n){
                j-=1;
                i+=1;
            }
            while(j>=0 && i<m){
                res[ind++]=mat[i][j];
                j-=1;
                i+=1;
            }
            j+=1;
            if(i==m){
                i-=1;
                j+=1;
            }

        }
        return res;
    }
}