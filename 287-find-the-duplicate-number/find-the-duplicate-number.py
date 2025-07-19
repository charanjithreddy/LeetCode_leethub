class Solution(object):
    def findDuplicate(self, nums):
        a=[0]*len(nums);
        for i in nums:
            if(a[i]>0):
                return i;
            a[i]+=1;
        """
        :type nums: List[int]
        :rtype: int
        """
        