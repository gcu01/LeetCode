1class Solution(object):
2    def minimumFlips(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        s = bin(n)[2:]
8        i, j = 0, len(s)-1
9        out = 0
10        while i < j:
11            if s[i] != s[j]:
12                out += 1
13            i += 1
14            j -= 1
15        return out*2