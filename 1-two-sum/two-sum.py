class Solution(object):
    def twoSum(self, nums, target):
        output=[];
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    output.append(i);
                    output.append(j);
        return output;
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        