1class Solution(object):
2    def earliestTime(self, tasks):
3        """
4        :type tasks: List[List[int]]
5        :rtype: int
6        """
7        minim = float('inf')
8        for i,j in tasks:
9            minim = min(minim, i+j)
10        return minim