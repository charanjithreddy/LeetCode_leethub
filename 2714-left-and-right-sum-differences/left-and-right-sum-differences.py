class Solution(object):
    def leftRightDifference(self, nums):
        l=[0];
        for i in nums[:-1]:
            l.append(l[-1]+i);
        r=[0];
        for i in nums[::-1]:
            r.append(r[-1]+i);
        r=r[::-1][1:]
        for i in range(len(l)):
            l[i]=abs(l[i]-r[i]);
        return l
        """
        :type nums: List[int]
        :rtype: List[int]
        """