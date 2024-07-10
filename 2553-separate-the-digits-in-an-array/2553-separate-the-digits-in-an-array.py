class Solution(object):
    def separateDigits(self, nums):
        o=[];
        for i in nums:
            if(i>9):
                s=[];
                while(i>0):
                    s.append(i%10);
                    i/=10;
                o+=s[::-1];
            else:
                o.append(i);
        return o;