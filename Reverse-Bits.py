1class Solution(object):
2    def reverseBits(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        out = 0
8        for i in range(32):
9            out = out << 1
10            out += (n & 1)
11            n = n >> 1
12        return out
13
14
15        sign = -1 if n<0 else 1
16        n = abs(n)
17        s = bin(n)[2:]
18        #print(s)
19        s = s[::-1]
20        #print(s)
21        out = sign * int(s, 2)
22        return out