class Solution(object):
    def boldWords(self, words, s):
        bold=[0]*len(s);
        for word in words:
            l=len(word);
            for i in range(len(s)-l+1):
                if(s[i:i+l]==word):
                    for j in range(i,i+l):
                        bold[j]=1;
        res="";
        for i in range(len(s)):
            if(i==0):
                if(bold[i]==1):
                    res+="<b>"
                res+=s[i]
            elif(i==len(s)-1):
                if(bold[i]==0):
                    if(bold[i-1]==1):
                        res+="</b>"
                    res+=s[i];
                else:
                    if(bold[i-1]==0):
                        res+="<b>"
                    res+=s[i]
                    res+="</b>"
            else:
                if(bold[i]==0):
                    if(bold[i-1]==1):
                        res+="</b>";
                    res+=s[i];
                if(bold[i]==1):
                    if(bold[i-1]==0):
                        res+="<b>";
                    res+=s[i];
        return res
                        
        """
        :type words: List[str]
        :type s: str
        :rtype: str
        """
        