class Solution(object):
    def checkStrings(self, s1, s2):
        s1_even=[];
        s1_odd=[];
        s2_even=[];
        s2_odd=[]
        for i in range(len(s1)):
            if(i%2==0):
                s1_even.append(s1[i]);
                s2_even.append(s2[i]);
            else:
                s1_odd.append(s1[i]);
                s2_odd.append(s2[i]);
        return sorted(s1_even)==sorted(s2_even) and sorted(s1_odd)==sorted(s2_odd)

        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        