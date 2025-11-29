int minOperations(int* nums, int numsSize, int k) {
    int res=0;
    for(int i=0;i<numsSize;i++){
        res=(res+nums[i])%k;
    }
    return res;
}