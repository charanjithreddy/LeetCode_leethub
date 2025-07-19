class Solution(object):
    def removeSubfolders(self, folder):
        folder.sort(key=lambda x:x.count('/'))
        o=set();
        for i in folder:
            x=1;
            for j in o:
                if(j+'/' in i and i.index(j+'/')==0):
                    x=0;
                    break;
            if(x==1):
                o.add(i);
        return list(o);
        """
        :type folder: List[str]
        :rtype: List[str]
        """