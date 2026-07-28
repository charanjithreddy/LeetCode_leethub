class Solution(object):
    def smallestPalindrome(self, s):
        t="";
        res="";
        arr=[0]*26;
        for i in s:
            arr[ord(i)-ord('a')]+=1;
        for i in range(len(arr)):
            if(arr[i]%2!=0):
                t+=chr(ord('a')+i);
                res+=chr(ord('a')+i)*(arr[i]//2);
            else:
                res+=chr(ord('a')+i)*(arr[i]//2);
        return res+t+res[::-1]
        """
        :type s: str
        :rtype: str
        """
        