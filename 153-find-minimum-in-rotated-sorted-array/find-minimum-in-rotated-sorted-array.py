class Solution(object):
    def findMin(self, nums):
        if(nums[0]<=nums[-1]):
            return nums[0];
        else:
            l=0;
            r=len(nums)-1;
            while(l<=r):
                mid=(l+r)//2;
                if(nums[l]<=nums[r]):
                    return nums[l];
                elif(nums[mid]>=nums[l]):
                    l=mid+1;
                else:
                    r=mid;
        """
        :type nums: List[int]
        :rtype: int
        """