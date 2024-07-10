class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        count=0;
        if(ruleKey=="type"):
            n=0;
        elif(ruleKey=="color"):
            n=1;
        else:
            n=2;
        for i in items:
            if(i[n]==ruleValue):
                count+=1;
        return count;
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        