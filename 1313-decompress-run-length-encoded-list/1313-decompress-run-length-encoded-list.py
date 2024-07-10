class Solution(object):
    def decompressRLElist(self, nums):
        o=[];
        for i in range(0,len(nums),2):
            o.extend([nums[i+1]]*nums[i]);
        return o;
                
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        