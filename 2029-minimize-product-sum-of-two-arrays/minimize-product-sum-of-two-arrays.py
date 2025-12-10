class Solution(object):
    def minProductSum(self, nums1, nums2):
        nums1.sort();
        nums2.sort();
        nums2=nums2[::-1];
        res=0;
        for i in range(len(nums1)):
            res+=(nums1[i]*nums2[i]);
        return res;
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        