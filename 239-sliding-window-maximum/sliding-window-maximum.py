class Solution(object):
    def maxSlidingWindow(self, nums, k):
        res=[];
        stack=[];
        for i in range(k):
            if(len(stack)==0):
                stack.append(nums[i]);
            elif(stack[-1]>=nums[i]):
                stack.append(nums[i]);
            else:
                while(len(stack)>0 and stack[-1]<nums[i]):
                    stack.pop(-1);
                stack.append(nums[i]);
        res.append(stack[0]);
        for i in range(k,len(nums)):
            if(stack[-1]>=nums[i]):
                stack.append(nums[i]);
            else:
                while(len(stack)>0 and stack[-1]<nums[i]):
                    stack.pop(-1);
                stack.append(nums[i]);
            if(stack[0]==nums[i-k]):
                stack.pop(0);
            res.append(stack[0]);
        return res;
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """