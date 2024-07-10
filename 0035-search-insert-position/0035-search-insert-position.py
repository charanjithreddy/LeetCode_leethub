class Solution(object):
    def searchInsert(self, nums, target):
        n=len(nums);
        if (target not in nums):
            if(target>nums[n-1]):
                return n;
            else:
                for i in range(n):
                    if(nums[i]>target):
                        return i;
                        break;

        else:
            for i in range(n):
                if(nums[i]==target):
                    return i;
                    break;
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        