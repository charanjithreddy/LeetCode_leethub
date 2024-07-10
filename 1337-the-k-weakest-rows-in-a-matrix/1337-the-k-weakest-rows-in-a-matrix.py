class Solution(object):
    def kWeakestRows(self, mat, k):
        s=[];
        for i in mat:
            s.append(i.count(1));
        o=[];
        for i in range(k):
            n=s.index(min(s));
            o.append(n);
            s[n]=max(s)+1;
        return o;