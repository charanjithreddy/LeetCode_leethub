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
        return folder;
        """
        :type folder: List[str]
        :rtype: List[str]
        """