class Solution(object):
    def calPoints(self, operations):
        res=[];
        for i in operations:
            if(i=='+'):
                res.append(res[-1]+res[-2]);
            elif(i=="D"):
                res.append(res[-1]*2);
            elif(i=="C"):
                res.pop(-1);
            else:
                res.append(int(i));
        return sum(res)
        """
        :type operations: List[str]
        :rtype: int
        """
        