class Solution(object):
    def kthCharacter(self, k):
        word="a";
        while(len(word)<k):
            temp=list(word);
            temp=[ord(i)+1 for i in temp];
            for i in range(len(temp)):
                if(temp[i]>122):
                    temp[i]-=26;
            temp=[chr(i) for i in temp];
            temp="".join(temp);
            word+=temp;
        return word[k-1];

        """
        :type k: int
        :rtype: str
        """
        