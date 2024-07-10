class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        d={};
        for i in items1:
            if(i[0] in d):
                d[i[0]]+=i[1];
            else:
                d[i[0]]=i[1];
        for i in items2:
            if(i[0] in d):
                d[i[0]]+=i[1];
            else:
                d[i[0]]=i[1];
        o=[];
        for i in sorted(d):
            o.append([i,d[i]]);
        return o;