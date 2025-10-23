class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        #improved solution

        buy = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif profit < (prices[i]-buy):
                profit = prices[i]-buy
        return profit

        #my solution
'''
        min = prices[0]        
        idx_min = 0  
        for i, value in enumerate(prices):
            if value < min:
                min = value
                idx_min = i

        if idx_min == len(prices): return 0
        
        max = prices[idx_min]
        idx_max = idx_min
        
        for j in range(idx_min+1, len(prices)):
            if prices[j] > max:
                max = prices[j]
                idx_max = j

        return (prices[idx_max]-prices[idx_min])
'''                