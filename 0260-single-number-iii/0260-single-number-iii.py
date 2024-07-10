class Solution(object):
    def singleNumber(self, nums):
        o=[];
        for i in set(nums):
            if(nums.count(i)==1):
                o.append(i);
        return o;