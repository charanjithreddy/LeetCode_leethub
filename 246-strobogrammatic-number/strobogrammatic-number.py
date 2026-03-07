class Solution(object):
    def isStrobogrammatic(self, num):
        d={"6":"9","9":"6","8":"8","0":"0","1":"1"};
        l=0;
        r=len(num)-1;
        while(l<=r):
            if(num[l] not in d or d[num[l]]!=num[r]):
                return False;
            l+=1;
            r-=1;
        return True;

        """
        :type num: str
        :rtype: bool
        """
        