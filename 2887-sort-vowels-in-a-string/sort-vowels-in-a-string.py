class Solution(object):
    def sortVowels(self, s):
        a=[];
        ind=[];
        vowels=['a','e','i','o','u','A','E','I','O','U'];
        for i in range(len(s)):
            if(s[i] in vowels):
                a.append(s[i]);
                ind.append(i);
        a.sort();
        s=list(s);
        for i in range(len(a)):
            s[ind[i]]=a[i];
        return "".join(s);

        """
        :type s: str
        :rtype: str
        """
        