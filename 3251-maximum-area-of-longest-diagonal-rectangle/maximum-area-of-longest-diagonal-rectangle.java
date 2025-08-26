class Solution {
    public int areaOfMaxDiagonal(int[][] dimensions) {
        int res_a=1,res_d=2;
        int l,w;
        for(int i=0;i<dimensions.length;i++){
            l=dimensions[i][0];
            w=dimensions[i][1];
            if(l*l+w*w>res_d){
                res_d=l*l+w*w;
                res_a=l*w;
            }
            res_a=(l*l+w*w==res_d && l*w>res_a)?l*w:res_a;
        }
        return res_a;
    }
}