class Solution(object):
    def findMaxK(self, nums):
        n=-1;
        for i in set(nums):
            if(i>0 and -1*i in nums and i>n):
                n=i;     
        return n;