class Solution(object):
    def maximumLength(self, nums):
        o=0;
        e=0;
        oe=[];
        eo=[];
        for i in nums:
            if(i%2==0):
                e+=1;
                if(len(eo)==0 or eo[-1]%2==1):
                    eo.append(i);
                if(len(oe)>0 and oe[-1]%2==1):
                    oe.append(i);
            else:
                o+=1;
                if(len(oe)==0 or oe[-1]%2==0):
                    oe.append(i);
                if(len(eo)>0 and eo[-1]%2==0):
                    eo.append(i);
        return max(o,e,len(oe),len(eo));
        """
        :type nums: List[int]
        :rtype: int
        """