class Solution(object):
    def removeSubfolders(self, folder):
        folder.sort(key=lambda x:x.count('/'))
        o=set();
        for i in range(len(folder)):
            j=i+1;
            while(j<len(folder)):
                if(folder[i]+'/'in folder[j] and folder[j].index(folder[i]+'/')==0):
                    folder.pop(j);
                else:
                    j+=1;
            """
            x=1;
            for j in o:
                s=j+'/';
                if(s in i and i.index(s)==0):
                    x=0;
                    break;
            if(x==1):
                o.add(i);"""
        return folder;
        """
        :type folder: List[str]
        :rtype: List[str]
        """