class Solution(object):
    def getModifiedArray(self, length, updates):
        a=[0]*length;
        for i in updates:
            a[i[0]]+=i[2];
            if(i[1]<length-1):
                a[i[1]+1]-=i[2];
        for i in range(1,length):
            a[i]+=a[i-1];
        return a;
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        