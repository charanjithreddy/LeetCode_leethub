class Solution(object):
    def getSneakyNumbers(self, nums):
        res=[];
        d={};
        for i in nums:
            if(i in d):
                d[i]+=1;
                if(d[i]==2):
                    res.append(i);
                    if(len(res)==2):
                        break;
            else:
                d[i]=1;
        return res;
            
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        