class Solution(object):
    def maximumLength(self, nums):
        o=0;
        e=0;
        comb=[];
        curr=nums[0]%2;
        for i in nums:
            if(i%2==0):
                e+=1;
                if(len(comb)==0 or curr==1):
                    comb.append(i);
                    curr=i%2;
            else:
                o+=1;
                if(len(comb)==0 or curr==0):
                    comb.append(i);
                    curr=i%2;
        return max(o,e,len(comb));
        """
        :type nums: List[int]
        :rtype: int
        """