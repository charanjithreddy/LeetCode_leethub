class Solution(object):
    def minOperations(self, nums, k):
        l=len(nums);
        count=-1;
        for i in range(l):
            output=True;
            for j in nums:
                if(j<k):
                    output=False;
                    break;
            nums.pop(nums.index(min(nums)));
            count+=1;
            if(output==True):
                break;
        return count;

        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        