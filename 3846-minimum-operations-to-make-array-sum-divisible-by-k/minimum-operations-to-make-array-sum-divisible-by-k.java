class Solution {
    public int minOperations(int[] nums, int k) {
        int res=0;
        for(int i:nums){
            res=(res+i)%k;
        }
        return res;
    }
}