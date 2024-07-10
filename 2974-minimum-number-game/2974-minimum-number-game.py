class Solution(object):
    def numberGame(self, nums):
        arr=[];
        for i in range(len(nums)/2):
            a=min(nums);
            nums.pop(nums.index(a));
            b=min(nums);
            nums.pop(nums.index(b));
            arr.append(b);
            arr.append(a);
        return arr;

        """
        :type nums: List[int]
        :rtype: List[int]
        """
        