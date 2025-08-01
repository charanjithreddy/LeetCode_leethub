class Solution(object):
    def generate(self, numRows):
        o=[];
        o.append([1]);
        for i in range(1,numRows):
            temp=[1,1];
            for j in range(len(o[-1])-1):
                temp.insert(-1,o[-1][j]+o[-1][j+1]);
            o.append(temp);
        return o;
        """
        :type numRows: int
        :rtype: List[List[int]]
        """