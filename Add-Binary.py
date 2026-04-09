1class Solution(object):
2    def addBinary(self, a, b):
3        """
4        :type a: str
5        :type b: str
6        :rtype: str
7        """
8        s = int(a,2)+int(b,2)
9        return str(bin(s))[2:]