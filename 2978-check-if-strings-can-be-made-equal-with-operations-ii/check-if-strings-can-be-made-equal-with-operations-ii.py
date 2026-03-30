class Solution(object):
    def checkStrings(self, s1, s2):
        s1_even=[0]*26;
        s1_odd=[0]*26;
        s2_even=[0]*26
        s2_odd=[0]*26
        for i in range(len(s1)):
            if(i%2==0):
                s1_even[ord(s1[i])-ord('a')]+=1
                s2_even[ord(s2[i])-ord('a')]+=1
            else:
                s1_odd[ord(s1[i])-ord('a')]+=1
                s2_odd[ord(s2[i])-ord('a')]+=1
        return (s1_even)==(s2_even) and (s1_odd)==(s2_odd)
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """