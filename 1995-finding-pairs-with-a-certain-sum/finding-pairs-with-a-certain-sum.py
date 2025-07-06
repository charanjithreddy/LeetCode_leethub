class FindSumPairs(object):    
    def __init__(self, nums1, nums2):
        self.nums1=nums1;
        self.nums2=nums2;
        self.d1={};
        self.d2={};
        for i in self.nums1:
            if(i in self.d1):
                self.d1[i]+=1;
            else:
                self.d1[i]=1;
        for i in self.nums2:
            if(i in self.d2):
                self.d2[i]+=1;
            else:
                self.d2[i]=1;
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
    def add(self, index, val):
        self.d2[self.nums2[index]]-=1;
        x=self.nums2[index]+val;
        if(x in self.d2):
            self.d2[x]+=1;
        else:
            self.d2[x]=1;
        self.nums2[index]+=val;
        """
        :type index: int
        :type val: int
        :rtype: None
        """
    def count(self, tot):
        c=0;
        for i in self.nums1:
            if(tot-i in self.d2):
                c+=self.d2[tot-i];
        return c;
        """
        :type tot: int
        :rtype: int
        """
# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)