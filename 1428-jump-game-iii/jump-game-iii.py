class Solution(object):
    def canReach(self, arr, start):
        self.res=False;
        def func(ind,s):
            if(self.res==True):
                return;
            if(ind in s):
                return;
            if(arr[ind]==0):
                self.res=True;
            s.add(ind);
            if(ind+arr[ind]<len(arr)):
                func(ind+arr[ind],s);
            if(ind-arr[ind]>=0):
                func(ind-arr[ind],s);
        func(start,set())
        return self.res;
        """
        :type arr: List[int]
        :type start: int
        :rtype: bool
        """
        