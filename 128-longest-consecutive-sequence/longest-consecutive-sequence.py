class Solution(object):
    def longestConsecutive(self, nums):
        o=0;
        nums=set(nums);
        for i in nums:
            if(i-1 not in nums):
                temp=i;
                while(temp+1 in nums):
                    temp+=1;
                o=max(o,temp-i+1)
        return o;
        """
        :type nums: List[int]
        :rtype: int
        """