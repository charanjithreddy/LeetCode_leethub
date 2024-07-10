class Solution(object):
    def minIncrementForUnique(self, nums):
        if(len(nums)==1):
            return 0;
        count=0;
        nums.sort();
        for i in range(1,len(nums)):
            if(nums[i]<=nums[i-1]):
                count+=1-(nums[i]-nums[i-1]);
                nums[i]=nums[i-1]+1;                
        return count;