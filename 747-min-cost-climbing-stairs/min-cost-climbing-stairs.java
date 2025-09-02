class Solution {
    static int min(int a,int b){
        if(a<b){
            return a;
        }
        else {
            return b;
        }
    }
    public int minCostClimbingStairs(int[] cost) {
        int a[]=new int[cost.length+1];
        for(int i=2;i<a.length;i++){
            a[i]=min(a[i-1]+cost[i-1],a[i-2]+cost[i-2]);
        }
        return a[a.length-1];        
    }
}