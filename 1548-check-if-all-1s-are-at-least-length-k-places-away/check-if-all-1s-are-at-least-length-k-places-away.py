class Solution(object):
    def kLengthApart(self, nums, k):
        ind=-1;
        for i in range(len(nums)):
            if(nums[i]==1):
                if(ind!=-1 and i-ind<=k):
                    return False;
                ind=i;
        return True;
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        