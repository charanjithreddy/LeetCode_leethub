class Solution(object):
    def canPartition(self, nums):
        if(sum(nums)%2==1):
            return False;
        target=sum(nums)/2;
        s=set();
        s.add(0);
        for i in nums:
            temp=set();
            for j in s:
                temp.add(i+j);
            if(target in temp):
                return True;
            s=s.union(temp);
        return False;

        """
        :type nums: List[int]
        :rtype: bool
        """
        