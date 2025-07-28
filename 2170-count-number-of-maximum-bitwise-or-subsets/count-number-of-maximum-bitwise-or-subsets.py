class Solution(object):
    def countMaxOrSubsets(self, nums):
        maxor=0;
        for i in nums:
            maxor|=i;
        o=[0];
        def func(i,curr_or):
            if(i==len(nums)):
                if(curr_or==maxor):
                    o[0]+=1;
                return;
            func(i+1,curr_or|nums[i-1]);
            func(i+1,curr_or);
        func(0,0);
        return o[0];
        """
        :type nums: List[int]
        :rtype: int
        """
        