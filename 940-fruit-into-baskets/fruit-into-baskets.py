class Solution(object):
    def totalFruit(self, fruits):
        o=0;
        d={};
        for i in range(len(fruits)):
            if(len(d)<2):
                if(fruits[i] in d):
                    d[fruits[i]]+=1;
                else:
                    d[fruits[i]]=1;
            elif(len(d)==2 and fruits[i] in d):
                d[fruits[i]]+=1;
            else:
                o=max(o,sum(list(d.values())));
                x=fruits[i-1];
                j=i-1;
                t=1;
                while(j>=0 and fruits[j-1]==x):
                    j-=1;
                    t+=1;
                d[x]=t
                for j in d:
                    if(j!=x):
                        x=j;
                        break;
                del d[x];
                d[fruits[i]]=1;
        return max(o,sum(list(d.values())));

        """
        :type fruits: List[int]
        :rtype: int
        """
        