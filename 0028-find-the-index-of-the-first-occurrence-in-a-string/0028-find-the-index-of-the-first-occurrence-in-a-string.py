class Solution(object):
    def strStr(self, haystack, needle):
        x=len(needle);
        y=len(haystack);
        if(x>y):
            return -1;
        else:
            output=0;
            for i in range(y-x+1):
                if(haystack[i:x+i]==needle):
                    output=1;
                    return i;
            if(output==0):
                return -1;
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        