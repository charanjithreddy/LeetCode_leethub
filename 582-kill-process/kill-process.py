class Solution(object):
    def killProcess(self, pid, ppid, kill):
        d={};
        for i in range(len(pid)):
            t=ppid[i];
            if(t in d):
                d[t].append(pid[i]);
            else:
                d[t]=[pid[i]];

        res=[];
        def func(val):
            res.append(val);
            if(val in d):
                for i in d[val]:
                    func(i);
        func(kill)
        return res;
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        