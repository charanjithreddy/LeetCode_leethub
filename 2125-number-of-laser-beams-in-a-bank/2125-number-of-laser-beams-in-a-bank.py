class Solution(object):
    def numberOfBeams(self, bank):
        l=[];
        for i in bank:
            n=i.count("1");
            if(n!=0):
                l.append(n);
        o=0;
        for i in range(len(l)-1):
            o+=l[i]*l[i+1]; 
        return o;
        """
        :type bank: List[str]
        :rtype: int
        """