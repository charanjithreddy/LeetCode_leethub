class Solution(object):
    def similarRGB(self, color):
        t=["00","11","22","33","44","55","66","77","88","99","aa","bb","cc","dd","ee","ff"]
        res="#";
        for i in range(1,len(color),2):
            inp=color[i:i+2];
            op=t[0];
            val=abs(int(inp,16)-int(t[0],16))
            for j in t[1:]:
                curr=abs(int(inp,16)-int(j,16))
                if(curr<val):
                    val=curr
                    op=j;
            res+=op;
        return res
        """
        :type color: str
        :rtype: str
        """
        