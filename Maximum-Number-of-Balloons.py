1class Solution(object):
2    def maxNumberOfBalloons(self, text):
3        """
4        :type text: str
5        :rtype: int
6        """
7        out = 999999
8        for ch in set("balloon"):
9            no1 = "balloon".count(ch)
10            no2 = text.count(ch)
11            if no1 > no2:
12                return 0
13            out = no2//no1 if (no2//no1) < out else out
14
15        return out