class Solution(object):
    def sortPeople(self, names, heights):
        o=[];
        d={};
        l=len(names);
        for i in range(l):
            d[heights[i]]=names[i];
        heights.sort(reverse=True);
        for i in range(l):
            o.append(d[heights[i]]);
        return o;