class Solution(object):
    def productExceptSelf(self, nums):
        left=[];
        left.append(nums[0]);
        for i in range(1,len(nums)):
            left.append(left[-1]*nums[i]);
        right=[];
        right.append(nums[-1]);
        for i in range(len(nums)-2,-1,-1):
            right.insert(0,right[0]*nums[i]);
        res=[];
        for i in range(len(nums)):
            if(i==0):
                res.append(right[i+1]);
            elif(i==len(nums)-1):
                res.append(left[i-1]);
            else:
                res.append(left[i-1]*right[i+1]);
        return res;
        """
        :type nums: List[int]
        :rtype: List[int]
        """