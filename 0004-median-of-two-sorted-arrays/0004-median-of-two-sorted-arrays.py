class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        for i in nums2:
            nums1.append(i);
        nums1.sort();
        n=len(nums1);
        if(n%2==0):
            return ((nums1[n//2]+nums1[(n//2)-1])/2.0);
        else:
            return nums1[n//2];
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        