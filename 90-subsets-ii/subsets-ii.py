class Solution(object):
    def subsetsWithDup(self, nums):
        o=[];
        nums.sort();
        def func(i,l):
            if(i==len(nums)):
                o.append(list(l));
                return;
            l.append(nums[i]);
            func(i+1,l);
            l.pop();
            while(i+1<len(nums) and nums[i+1]==nums[i]):
                i+=1;
            func(i+1,l);
        func(0,[]);
        return o;
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        