class Solution(object):
    def isValid(self, word):
        vowels=['a','e','i','o','u','A','E','I','O','U'];
        v=0;
        c=0;
        if(len(word)<3 or not(word.isalnum())):
            return False;
        for i in word:
            if(i in vowels):
                v+=1;
                if(v>=1 and c>=1):
                    return True;
            elif(i.isalpha()):
                c+=1;
                if(v>=1 and c>=1):
                    return True;
        return v>=1 and c>=1;

        """
        :type word: str
        :rtype: bool
        """
        