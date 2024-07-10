class Solution(object):
    def searchRange(self, nums, target):
        l=len(nums);
        output=[];
        if (target in nums):
            output.append(nums.index(target));
            nums=nums[::-1];
            output.append(l-1-nums.index(target));
            return output;
        else:
            return [-1,-1];

        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        