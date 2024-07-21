class Solution(object):
    def getCommon(self, nums1, nums2):
        if(len(nums1)>len(nums2)):
            for i in nums2:
                begin=0;
                end=len(nums1)-1;
                while(begin<=end):
                    mid=(begin+end)//2;
                    if(nums1[mid]==i):
                        return nums1[mid];
                    elif(nums1[mid]<i):
                        begin=mid+1;
                    else:
                        end=mid-1;
        else:
            for i in nums1:
                begin=0;
                end=len(nums2)-1;
                while(begin<=end):
                    mid=(begin+end)//2;
                    if(nums2[mid]==i):
                        return nums2[mid];
                    elif(nums2[mid]<i):
                        begin=mid+1;
                    else:
                        end=mid-1;
        return -1;

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        