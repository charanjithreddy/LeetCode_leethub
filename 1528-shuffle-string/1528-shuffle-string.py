class Solution(object):
    def restoreString(self, s, indices):
        o=[];
        l=len(indices);
        o=['']*l;
        for i in range(l):
            o[indices[i]]=s[i];
        return ''.join(o);
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """