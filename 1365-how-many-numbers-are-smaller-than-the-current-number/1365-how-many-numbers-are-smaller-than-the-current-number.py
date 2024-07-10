class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        s=sorted(nums);
        o=[];
        for i in nums:
            o.append(s.index(i));
        return o;
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        