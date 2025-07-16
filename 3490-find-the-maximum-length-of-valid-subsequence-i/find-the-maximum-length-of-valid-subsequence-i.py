class Solution(object):
    def maximumLength(self, nums):
        o=0;
        e=0;
        comb=[];
        for i in nums:
            if(i%2==0):
                e+=1;
                if(len(comb)==0):
                    comb.append(i);
                elif(comb[-1]%2==1):
                    comb.append(i);
                
            else:
                o+=1;
                if(len(comb)==0):
                    comb.append(i);
                elif(comb[-1]%2==0):
                    comb.append(i);
        return max(o,e,len(comb));
        """
        :type nums: List[int]
        :rtype: int
        """