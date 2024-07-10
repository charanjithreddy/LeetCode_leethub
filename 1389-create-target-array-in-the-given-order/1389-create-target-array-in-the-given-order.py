class Solution(object):
    def createTargetArray(self, nums, index):
        t=[];
        for i in range(len(index)):
            t.insert(index[i],nums[i]);
        return t;
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """        