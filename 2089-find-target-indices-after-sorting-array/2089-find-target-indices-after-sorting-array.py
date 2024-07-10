class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort();
        o=[];
        for i in range(len(nums)):
            if(nums[i]==target):
                o.append(i);
        return o;