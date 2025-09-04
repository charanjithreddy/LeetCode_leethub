class Solution {
    public int findClosest(int x, int y, int z) {
        int d1=z-x<0?-1*(z-x):z-x;
        int d2=z-y<0?-1*(z-y):z-y;
        if(d1<d2){
            return 1;
        }
        else if(d1>d2){
            return 2;
        }
        else{
            return 0;
        }
    }
}