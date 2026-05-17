1class Solution(object):
2    def hammingWeight(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        s = str(bin(n)[2:])
8        #print(bin(n)[2:])
9        #print("s = ", s)
10        i, out = 0, 0
11        while i < len(s):
12            #print("s[i]=", s[i])
13            if s[i] == "1":
14                out += 1
15            i += 1
16        return out