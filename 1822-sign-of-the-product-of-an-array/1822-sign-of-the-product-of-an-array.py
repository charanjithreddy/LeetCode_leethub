class Solution(object):
    def arraySign(self, nums):
        if(0 in nums):
            return 0;
        n=0;
        for i in nums:
            if(i<0):
                n+=1;
        if(n%2==0):
            return 1;
        else:
            return -1;