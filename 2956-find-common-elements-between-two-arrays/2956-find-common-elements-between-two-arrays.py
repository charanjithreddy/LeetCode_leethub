class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        answer1=0;
        answer2=0;
        for i in nums1:
            if(i in nums2):
                answer1+=1;
        for i in nums2:
            if(i in nums1):
                answer2+=1;
        return [answer1,answer2];