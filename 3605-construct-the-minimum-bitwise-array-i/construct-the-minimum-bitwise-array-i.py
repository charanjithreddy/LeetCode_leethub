class Solution(object):
    def minBitwiseArray(self, nums):
        res=[];
        for i in nums:
            flag=1;
            for j in range(i):
                if(j|(j+1)==i):
                    res.append(j);
                    flag=0;
                    break;
            if(flag==1):
                res.append(-1);
        return res;
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        