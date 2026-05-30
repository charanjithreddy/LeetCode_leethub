class Solution(object):
    def confusingNumber(self, n):
        d={"0":"0","1":"1","6":"9","8":"8","9":"6"};
        res="";
        for i in str(n)[::-1]:
            if(i not in d):
                return False;
            res+=d[i];
        return res!=str(n)
        """
        :type n: int
        :rtype: bool
        """
        