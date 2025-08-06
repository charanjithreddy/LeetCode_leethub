class Solution(object):
    def letterCombinations(self, digits):
        d={2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"};
        o=[];
        if(len(digits)==0):
            return o;
        def func(i,s):
            if(i==len(digits)):
                o.append(s);
                return;
            for j in d[int(digits[i])]:
                s+=j;
                func(i+1,s);
                s=s[:i];
        func(0,"");
        return o;          

        """
        :type digits: str
        :rtype: List[str]
        """
        