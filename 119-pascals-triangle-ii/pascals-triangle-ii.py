class Solution(object):
    def getRow(self, rowIndex):
        l=[[1]];
        for i in range(1,rowIndex+1):
            t=[0]+l[i-1]+[0];
            temp=[];
            for j in range(len(t)-1):
                temp.append(t[j]+t[j+1]);
            l.append(temp);
        return l[rowIndex]

        """
        :type rowIndex: int
        :rtype: List[int]
        """
        