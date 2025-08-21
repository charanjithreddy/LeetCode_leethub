class Solution(object):
    def canJump(self, nums):
        a=[0]*len(nums);
        a[0]=1;
        i=0;
        while(True):
            if(i>=len(nums)):
                return False;
            if(a[-1]==1):
                return True;
            if(a[i]==1):
                for j in range(1,nums[i]+1):
                    if(i+j<len(nums)):
                        a[i+j]=1;
                    else:
                        break;
            i+=1;
        """
        :type nums: List[int]
        :rtype: bool
        """
        