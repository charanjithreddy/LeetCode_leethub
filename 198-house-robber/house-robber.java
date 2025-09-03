class Solution {
    static int max(int a,int b){
        if(a>b){
            return a;
        }
        else{
            return b;
        }
    }
    public int rob(int[] nums) {
        if(nums.length==1){
            return nums[0];
        }
        else if(nums.length==2){
            return max(nums[0],nums[1]);
        }
        else{
            int m=0;
            for(int i=2;i<nums.length;i++){
                m=max(m,nums[i-2]);
                nums[i]=max(m+nums[i],nums[i-1]);
            }
            return nums[nums.length-1];
        }
        
    }
}