class Solution(object):
    def mergeAlternately(self, word1, word2):
        l1=len(word1);
        l2=len(word2);
        if(l1==0 & l2==0):
            return "";
        elif(l1==0):
            return word2;
        elif(l2==0):
            return word1;
        if(l1>l2):
            output="";
            for i in range(l2):
                output+=(word1[i]+word2[i]);
            return output+word1[l2:l1];
        else:
            output="";
            for i in range(l1):
                output+=(word1[i]+word2[i]);
            return output+word2[l1:l2];
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        