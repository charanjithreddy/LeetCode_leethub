class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        o=0;
        for i in jewels:
            o+=stones.count(i);
        return o;