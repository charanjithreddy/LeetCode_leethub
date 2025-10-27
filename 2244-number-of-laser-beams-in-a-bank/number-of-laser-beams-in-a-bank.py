class Solution(object):
    def numberOfBeams(self, bank):
        res=0;
        cur=0;
        for i in bank:
            temp=i.count('1');
            if(temp==0):
                continue;
            res+=cur*temp;
            cur=temp;
        return res;
        """
        :type bank: List[str]
        :rtype: int
        """
        