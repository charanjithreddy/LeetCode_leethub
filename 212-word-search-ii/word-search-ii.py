class Node():
    def __init__(self):
        self.next={};
        self.end=False;
class Solution(object):
    def findWords(self, board, words):
        root=Node();
        for i in words:
            temp=root;
            for j in i:
                if(j not in temp.next):
                    temp.next[j]=Node();
                temp=temp.next[j];
            temp.end=True;
        m=len(board);
        n=len(board[0]);
        visited=[[0]*n for i in range(m)];
        res=set()
        def func(r,c,word,node):
            if(r<0 or c<0 or r==m or c==n or visited[r][c]==1 or board[r][c] not in node.next):
                return ;
            visited[r][c]=1;
            node=node.next[board[r][c]];
            word+=board[r][c];
            if(node.end):
                res.add(word);
            func(r+1,c,word,node);
            func(r-1,c,word,node);
            func(r,c+1,word,node);
            func(r,c-1,word,node);
            visited[r][c]=0;
        
        for i in range(m):
            for j in range(n):
                func(i,j,"",root);
        return list(res);
            



        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        