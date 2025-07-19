class Solution(object):
    def removeSubfolders(self, folder):
        o=[];
        for i in sorted(folder):
            x=1;
            for j in range(len(i)):
                if((i[j]=="/") and i[:j] in o):
                    x=0;
                    break;
            if(x==1):
                o.append(i);
        return o;
        """
        :type folder: List[str]
        :rtype: List[str]
        """