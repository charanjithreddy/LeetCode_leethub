class Solution(object):
    def intersect(self, nums1, nums2):
        output=[];
        l1=len(nums1);
        l2=len(nums2);
        if(l1>l2):
            for i in range(l2):
                if(nums2[i] in nums1):
                    output.append(nums2[i]);
                    nums1.pop(nums1.index(nums2[i]));
            return output;
        else:
            for i in range(l1):
                if(nums1[i] in nums2):
                    output.append(nums1[i]);
                    nums2.pop(nums2.index(nums1[i]));
            return output;



        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        