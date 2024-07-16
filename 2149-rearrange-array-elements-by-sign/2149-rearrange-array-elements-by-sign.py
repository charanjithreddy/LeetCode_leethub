class Solution(object):
    def rearrangeArray(self, nums):
        o=[1]*len(nums);
        pos=0;
        neg=1;
        for i in nums:
            if(i>0):
                o[pos]=i;
                pos+=2;
            else:
                o[neg]=i;
                neg+=2;
        return o;