class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort();
        trainers.sort();
        o=0;
        p=0;
        t=0
        while(t<len(trainers) and p<len(players)):
            if(players[p]<=trainers[t]):
                o+=1;
                p+=1;
            t+=1;
        return o;
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """