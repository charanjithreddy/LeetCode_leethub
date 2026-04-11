class Solution(object):
    def minimumDistance(self, nums):
        d={};
        for i in range(len(nums)):
            if(nums[i] in d):
                d[nums[i]].append(i);
            else:
                d[nums[i]]=[i];
        res=-1;
        for i in d:
            if(len(d[i])>=3):
                d[i].sort();
                for x in range(len(d[i])-2):
                    if(res==-1):
                        res=2*(max(d[i][x],d[i][x+1],d[i][x+2])-min(d[i][x],d[i][x+1],d[i][x+2]))
                    else:
                        res=min(res,2*(max(d[i][x],d[i][x+1],d[i][x+2])-min(d[i][x],d[i][x+1],d[i][x+2])))
        return res
        """
        :type nums: List[int]
        :rtype: int
        """
        