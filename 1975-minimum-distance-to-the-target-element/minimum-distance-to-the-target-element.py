class Solution(object):
    def getMinDistance(self, nums, target, start):
        i=0;
        while(start+i<len(nums) or start-i>=0):
            if(start+i<len(nums) and nums[start+i]==target):
                return i;
            if(start-i>=0 and nums[start-i]==target):
                return i;
            i+=1;
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        