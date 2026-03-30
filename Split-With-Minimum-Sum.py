1class Solution(object):
2    def splitNum(self, num):
3        """
4        :type num: int
5        :rtype: int
6        """
7        s = "".join(sorted(str(num)))
8        return int(s[::2]) +int(s[1::2])
9
10        digits = [int(d) for d in str(n)]
11        digits.sort()
12        print(digits)
13        n = len(digits)
14        n1, n2 = [], []
15        for i in range(n//2):
16            n1.insert[i]