class Solution(object):
    def findDifferentBinaryString(self, nums):
        res=[];
        def func(i,s):
            if(i==len(nums)):
                if(s not in nums):
                    res.append(s);
                return;
            func(i+1,s+"0");
            func(i+1,s+"1");
        func(0,"");
        return res[0]
        """
        :type nums: List[str]
        :rtype: str
        """
        