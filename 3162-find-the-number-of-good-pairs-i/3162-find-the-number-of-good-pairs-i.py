class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        count=0;
        for i in nums1:
            for j in nums2:
                if(i>=j and i%(j*k)==0):
                    count+=1;
        return count;
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        