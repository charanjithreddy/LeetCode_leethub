class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        s=set();
        for i in range(min(k,len(nums))):
            if(nums[i] in s):
                return True;
            s.add(nums[i]);
        i=0;
        j=min(k,len(nums));
        while(j<len(nums)):
            if(nums[j] in s):
                return True;
            s.add(nums[j]);
            s.remove(nums[i]);
            i+=1;
            j+=1;
        return False;
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """