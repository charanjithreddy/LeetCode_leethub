class Solution(object):
    def pivotArray(self, nums, pivot):
        l=[];
        e=[];
        g=[];
        for i in nums:
            if(i<pivot):
                l.append(i);
            elif(i==pivot):
                e.append(i);
            else:
                g.append(i);
        return l+e+g
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        