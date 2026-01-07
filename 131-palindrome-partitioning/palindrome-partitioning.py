class Solution(object):
    def partition(self, s):
        res=[];
        temp=[];
        def func(i):
            if(i==len(s)):
                res.append(list(temp));
                return;
            for j in range(i,len(s)):
                if(s[i:j+1]==s[i:j+1][::-1]):
                    temp.append(s[i:j+1]);
                    func(j+1);
                    temp.pop(-1);
        func(0);
        return res;
        """
        :type s: str
        :rtype: List[List[str]]
        """
        