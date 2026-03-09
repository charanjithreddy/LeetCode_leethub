class Solution(object):
    def canJump(self, nums):
        a=[0]*len(nums);
        a[0]=1;
        for i in range(len(nums)):
            if(a[i]==1):
                for j in range(i+1,min(len(nums),i+nums[i]+1)):
                    a[j]=1;
            else:
                break;
            if(a[-1]==1):
                break;
        return a[-1]==1
        """
        :type nums: List[int]
        :rtype: bool
        """
        