class Solution(object):
    def maximum69Number (self, num):
        s=[];
        while(num>0):
            s.append(num%10);
            num/=10;
        for i in range(len(s)-1,-1,-1):
            if(s[i]==6):
                s[i]=9;
                break;
        n="";
        for i in s:
            n+=str(i);
        return int(n[::-1]);