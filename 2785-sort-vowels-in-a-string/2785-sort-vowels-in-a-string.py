class Solution(object):
    def sortVowels(self, s):
        vowels=['a','e','i','o','u','A','E','I','O','U']
        t=sorted([i for i in s if i in vowels]);
        if(len(t)==1 or len(t)==0):
            return s;
        o="";
        x=0
        for i in s:
            if(i in vowels):
                o+=t[x];
                x+=1;
            else:
                o+=i;
        return o;