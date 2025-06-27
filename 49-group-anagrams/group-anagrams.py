class Solution(object):
    def groupAnagrams(self, strs):
        d={};
        for i in strs:
            if("".join(sorted(i)) in d):
                d["".join(sorted(i))].append(i);
            else:
                d["".join(sorted(i))]=[i];
        return [d[i] for i in d];
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """