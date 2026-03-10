1class Solution(object):
2    def numJewelsInStones(self, jewels, stones):
3        """
4        :type jewels: str
5        :type stones: str
6        :rtype: int
7        """
8        res = 0
9        for val in jewels:
10            res += stones.count(val)
11        return res