class Solution(object):
    def coinChange(self, coins, amount):
        arr=[-1]*(amount+1)
        arr[0]=0;
        coins.sort()
        for i in range(amount+1):
            if(arr[i]==-1):
                continue
            for coin in coins:
                if(i+coin>amount):
                    break
                if(arr[i+coin]==-1):
                    arr[i+coin]=arr[i]+1;
                else:
                    arr[i+coin]=min(arr[i+coin],arr[i]+1);
        return arr[-1]




        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        