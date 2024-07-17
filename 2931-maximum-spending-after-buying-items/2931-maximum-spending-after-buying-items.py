class Solution(object):
    def maxSpending(self, values):
        o=[];
        for i in values:
            for j in i:
                o.append(j);
        o.sort();
        sum=0;
        for i in range(len(o)):
            sum+=(i+1)*o[i];
        return sum;
        """
        :type values: List[List[int]]
        :rtype: int
        """
        