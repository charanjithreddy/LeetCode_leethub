class Solution(object):
    def sortArrayByParity(self, nums):
        o=[];e=[]
        for i in nums:
            if(i%2==0):
                e.append(i);
            else:
                o.append(i);
        return e+o;