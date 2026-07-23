class Solution(object):
    def uniqueXorTriplets(self, nums):
        n=len(nums);
        if(n>=3):
            return int(2**(floor(math.log(n,2))+1))
        else:
            return n;
        """
        :type nums: List[int]
        :rtype: int
        """
        