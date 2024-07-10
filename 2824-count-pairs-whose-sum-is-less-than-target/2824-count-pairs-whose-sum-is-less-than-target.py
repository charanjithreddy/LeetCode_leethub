class Solution(object):
    def countPairs(self, nums, target):
        count=0;
        l=len(nums);
        for i in range(l):
            for j in range(i+1,l):
                if(nums[i]+nums[j]<target):
                    count+=1;
        return count;
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        