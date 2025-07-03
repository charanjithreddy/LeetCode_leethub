class Solution(object):
    def kthCharacter(self, k):
        word=["a"];
        while(len(word)<k):
            if(k-1<len(word)):
                return word[k-1];
            temp=[ord(i)+1 for i in word];
            for i in range(len(temp)):
                if(temp[i]>122):
                    temp[i]-=26;
            temp=[chr(i) for i in temp];
            word.extend(temp);
        return word[k-1];
        """
        :type k: int
        :rtype: str
        """