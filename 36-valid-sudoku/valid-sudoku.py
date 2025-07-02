class Solution(object):
    def isValidSudoku(self, board):
        for  i in board:
            a=[0]*10;
            for j in i:
                if(j!="."):
                    j=int(j);
                    a[j]+=1;
                    if(a[j]>1):
                        return False;
        for i in range(len(board)):
            x=[];
            for j in range(len(board)):
                x.append(board[j][i]);
            a=[0]*10;
            for j in x:
                if(j!="."):
                    j=int(j);
                    a[j]+=1;
                    if(a[j]>1):
                        return False;
        for i in range(3):
            for j in range(3):
                x=[];
                for r in range(3*i,(i+1)*3):
                    for c in range(3*j,(j+1)*3):
                        x.append(board[r][c]);
                a=[0]*10;
                for ele in x:
                    if(ele!="."):
                        ele=int(ele);
                        a[ele]+=1;
                        if(a[ele]>1):
                            return False;             
        return True;
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        