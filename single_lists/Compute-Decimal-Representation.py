1class Solution(object):
2    def decimalRepresentation(self, n):
3        """
4        :type n: int
5        :rtype: List[int]
6        """
7        digits = len(str(n))
8        #print(digits)
9        i = 0
10        out = []
11        while i < digits:
12            rem = n % 10
13            n /= 10
14            out.append(rem * 10**i)
15            i += 1
16        #out.reverse()
17        out = [x for x in out if x != 0]
18        return out[::-1]