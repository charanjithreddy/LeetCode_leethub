class Solution(object):
    def groupAnagrams(self, strs):
        d={};
        for i in strs:
            x="".join(sorted(i));
            if(x in d):
                d[x].append(i);
            else:
                d[x]=[i];
        return [d[i] for i in d];
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """