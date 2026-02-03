class Solution(object):
    def isTrionic(self, nums):
        p=0;
        flag1,flag2,flag3=0,0,0;
        while(p<len(nums)-1):
            if(nums[p+1]>nums[p]):
                flag1=1;
                p+=1;
            else:
                break;
        if(flag1==0):
            return False;
        q=p;
        while(q<len(nums)-1):
            if(nums[q+1]<nums[q]):
                flag2=1;
                q+=1;
            else:
                break;
        r=q;
        if(flag2==0):
            return False;
        while(r<len(nums)-1):
            if(nums[r+1]>nums[r]):
                flag3=1;
                r+=1;
            else:
                break;
        return r==len(nums)-1 and flag3==1;
        """
        :type nums: List[int]
        :rtype: bool
        """