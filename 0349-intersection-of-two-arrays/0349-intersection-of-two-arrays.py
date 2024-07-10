class Solution(object):
    def intersection(self, nums1, nums2):
        o=[];
        if(len(nums1)>len(nums2)):
            for i in nums2:
                if(i in nums1):
                    o.append(i);
        else:
            for i in nums1:
                if(i in nums2):
                    o.append(i);
        return set(o);