class Solution {
    static int max(int a,int b){
        if(a>b){
            return a;
        }
        else{
            return b;
        }
    }
    public int areaOfMaxDiagonal(int[][] dimensions) {
        int res_a=1,res_d=2;
        for(int i=0;i<dimensions.length;i++){
            int l=dimensions[i][0];
            int w=dimensions[i][1];
            if(l*l+w*w>res_d){
                res_d=l*l+w*w;
                res_a=l*w;
            }
            else if(l*l+w*w==res_d){
                res_a=max(res_a,l*w);
            }
        }
        return res_a;
    }
}