class Solution(object):
    def maximumUniqueSubarray(self, nums):
        left=0;
        right=0;
        o=0;
        s=nums[left];
        a=set();
        a.add(nums[left])
        while(right<len(nums)-1):
            if(nums[right+1] not in a):
                right+=1;
                s+=nums[right];
                a.add(nums[right]);
            else:
                o=max(o,s);
                while(nums[left]!=nums[right+1]):
                    a.remove(nums[left]);
                    s-=nums[left];
                    left+=1;
                s-=nums[left];
                a.remove(nums[left]);
                left+=1;

        o=max(o,s);
        return o;
        """
        :type nums: List[int]
        :rtype: int
        """