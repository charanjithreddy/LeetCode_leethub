class Solution(object):
    def targetIndices(self, nums, target):
        res=[];
        nums.sort();
        for ind,num in enumerate(nums):
            if(num==target):
                res.append(ind);
        return res
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        