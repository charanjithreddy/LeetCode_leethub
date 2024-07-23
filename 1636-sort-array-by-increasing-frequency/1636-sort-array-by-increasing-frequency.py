class Solution(object):
    def frequencySort(self, nums):
        output=[];
        d={};
        l=0;
        for i in nums:
            if i not in d:
                d[i]=1;
                if(d[i]>l):
                    l=d[i];
            else:
                d[i]+=1;
                if(d[i]>l):
                    l=d[i];
        for i in range(l+1):
            s=[];
            for j in d:
                if d[j]==i:
                    s.append(j);
            s.sort(reverse=True);
            for j in s:
                output+=[j]*i;
        return output;
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        