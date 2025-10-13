class Solution(object):
    def removeAnagrams(self, words):
        o=[];
        for i in words:
            t=[0]*26;
            for j in i:
                t[ord(j)-ord('a')]+=1;
            o.append("".join([str(x) for x in t]));
        
        i=1;
        while(i<len(words)):
            if(o[i]==o[i-1]):
                o.pop(i);
                words.pop(i);
            else:
                i+=1;
        return words;
        """
        :type words: List[str]
        :rtype: List[str]
        """