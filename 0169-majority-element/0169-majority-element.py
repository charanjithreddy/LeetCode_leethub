class Solution(object):
    def majorityElement(self, nums):
        l=len(nums)/2;
        for i in set(nums):
            if(nums.count(i)>l):
                return i;

                
        """
        :type nums: List[int]
        :rtype: int
        """
        