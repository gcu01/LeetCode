1class Solution(object):
2    def maximumValue(self, strs):
3        """
4        :type strs: List[str]
5        :rtype: int
6        """
7        maxim = 0
8        for val in strs:
9            try:
10                num = int(val)
11                if maxim < num:
12                    maxim = num
13            except ValueError:
14                if maxim < len(val):
15                    maxim = len(val)
16        return maxim