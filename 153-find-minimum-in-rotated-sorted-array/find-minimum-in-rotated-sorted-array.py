class Solution(object):
    def findMin(self, nums):
        l=0;
        r=len(nums)-1;
        while(l<=r):
            if(nums[l]<=nums[r]):
                return nums[l];
            else:
                mid=(l+r)//2;
                if(nums[mid]>nums[r]):
                    l=mid+1;
                elif(nums[mid]<nums[l]):
                    r=mid;
        """
        :type nums: List[int]
        :rtype: int
        """
        