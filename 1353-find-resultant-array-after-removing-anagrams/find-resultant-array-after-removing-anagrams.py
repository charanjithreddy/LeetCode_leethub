class Solution(object):
    def removeAnagrams(self, words):
        o=[];
        i=0;
        while(i<len(words)):
            t=[0]*26;
            for j in words[i]:
                t[ord(j)-ord('a')]+=1;
            if(len(o)==0):
                o.append("".join([str(x) for x in t]));
                i+=1;
            elif("".join([str(x) for x in t])==o[-1]):
                words.pop(i);
            else:
                o.append("".join([str(x) for x in t]));
                i+=1;
        return words;
        """
        :type words: List[str]
        :rtype: List[str]
        """