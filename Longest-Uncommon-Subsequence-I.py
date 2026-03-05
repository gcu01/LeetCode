1class Solution(object):
2    def findLUSlength(self, a, b):
3        """
4        :type a: str
5        :type b: str
6        :rtype: int
7        """
8        if a==b:
9            return -1
10        return max(len(a), len(b))
11
12        '''
13        if a=="":
14            return b
15        elif b=="":
16            return a
17        elif a==b:
18            return -1
19        l1, l2 = a[0], b[0]
20        for i in range(1, len(a)):
21            if l1 not in b: 
22                l1 += a[i]
23            else:
24                l1=""+a[i]
25        for i in range(1, len(b)):
26            if l2 not in b: 
27                l2 += b[i]
28            else:
29                break
30        return len(l1) if len(l1)>=len(l2) else len(l2)
31        '''