class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        p=[];a=[];
        for i in arr2:
            p+=[i]*(arr1.count(i));
        for i in sorted(arr1):
            if(i not in arr2):
                p.append(i);
        return p;