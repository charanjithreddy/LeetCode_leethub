class Solution {
    static int abs(int a){
        if(a<0){
            a*=-1;
        }
        return a;
    }
    public int findClosest(int x, int y, int z) {
        if(abs(z-x)<abs(z-y)){
            return 1;
        }
        else if(abs(z-x)>abs(z-y)){
            return 2;
        }
        else{
            return 0;
        }
    }
}