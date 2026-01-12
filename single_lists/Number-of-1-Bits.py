1class Solution(object):
2    def hammingWeight(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        s = bin(n)[2:]
8        return s.count("1")