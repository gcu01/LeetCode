1class Solution(object):
2    def countCompleteDayPairs(self, hours):
3        """
4        :type hours: List[int]
5        :rtype: int
6        """
7        out = 0
8        for i in range(len(hours)):
9            for j in range(i+1, len(hours) ):
10                if (hours[i]+hours[j]) % 24 == 0:
11                    out += 1
12        return out 