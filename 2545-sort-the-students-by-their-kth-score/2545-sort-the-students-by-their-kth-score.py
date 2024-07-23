class Solution(object):
    def sortTheStudents(self, score, k):
        marks={};
        for i in range(len(score)):
            marks[i]=score[i][k];
        o=[];
        sample=[];
        for i in marks.values():
            sample.append(i);
        sample.sort(reverse=True);
        for i in sample:
            for j in marks:
                if(marks[j]==i):
                    o.append(score[j]);
        return o;
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """