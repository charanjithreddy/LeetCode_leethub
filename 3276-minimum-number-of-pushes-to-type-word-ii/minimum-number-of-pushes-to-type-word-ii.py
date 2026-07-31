class Solution(object):
    def minimumPushes(self, word):
        alpha=[];occ=[];
        for i in list(set(word)):
            alpha.append(i);
            occ.append(word.count(i));
        d={};
        number=c=1;
        while(max(occ)>0):
            n=occ.index(max(occ));
            d[alpha[n]]=number;
            occ[n]=0;
            c+=1;
            if(c>8):
                c=1;
                number+=1;
        output=0
        for i in word:
            output+=d[i];
        return output;
        """
        :type word: str
        :rtype: int
        """
        