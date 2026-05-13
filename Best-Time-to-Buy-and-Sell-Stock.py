1class Solution(object):
2    def maxProfit(self, prices):
3        """
4        :type prices: List[int]
5        :rtype: int
6        """
7        if len(prices) < 2:
8            return 0
9        buy = prices[0]
10        profit = 0
11
12        for i in range(1, len(prices)):
13            if prices[i] < buy:
14                buy = prices[i]
15            elif profit < prices[i] - buy:
16                profit = prices[i] - buy
17        return profit
18
19        out = 0
20        for i in range(len(prices)):
21            maxx = max(prices[i:])
22            if out < (maxx-prices[i]):
23                out = maxx-prices[i]
24
25        return out
26
27
28
29
30        minn = min(prices[:-1])
31        idx = prices[:-1].index(minn)
32        maxx = max(prices[idx:])
33        print("min=", minn, "   idx=", idx, "   maxx=", maxx)
34        return maxx - minn
35        