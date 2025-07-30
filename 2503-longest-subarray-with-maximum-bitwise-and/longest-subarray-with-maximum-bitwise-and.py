class Solution(object):
    def longestSubarray(self, nums):
        m=max(nums);
        o=1;
        curr=0;
        for i in nums:
            if(i==m):
                curr+=1;
            else:
                o=max(o,curr);
                curr=0;
        
        return max(o,curr);           

        """
        :type nums: List[int]
        :rtype: int
        """
        