1class Solution(object):
2    def buyChoco(self, prices, money):
3        """
4        :type prices: List[int]
5        :type money: int
6        :rtype: int
7        """
8        prices.sort()
9        #print(prices)
10        
11        if (prices[0]+prices[1])<=money:
12            return money-prices[0]-prices[1]
13        return money