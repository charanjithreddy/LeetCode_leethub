class Solution(object):
    def longestSubarray(self, nums):
        m=max(nums);
        o=1;
        curr=0;
        for i in nums:
            if(i==m):
                curr+=1;
            else:
                if(curr>o):
                    o=curr;
                curr=0;
        if(curr>o):
            return curr;
        else:
            return o;       
        """
        :type nums: List[int]
        :rtype: int
        """       