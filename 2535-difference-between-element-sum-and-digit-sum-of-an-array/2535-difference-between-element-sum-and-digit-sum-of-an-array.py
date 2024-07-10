class Solution(object):
    def sumofdigits(self,n):
        if(n<10):
            return n;
        else:
            return n%10 + self.sumofdigits(n/10);
    def differenceOfSum(self, nums):
        esum=sum(nums);
        dsum=0;
        for i in nums:
            if(i<10):
                dsum+=i;
            else:
                dsum+=self.sumofdigits(i);
        return abs(esum-dsum);