1class Solution(object):
2    def backspaceCompare(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: bool
7        """
8        ls = list(s)
9        #print(ls)
10        while "#" in ls:
11            idx = ls.index("#")
12            if idx > 0:
13                ls = ls[:idx-1] + ls[idx+1:]
14            else:
15                ls = ls[idx+1:]
16        #print(ls)
17
18        lt = list(t)
19        #print(lt)
20        while "#" in lt:
21            idx = lt.index("#")
22            if idx > 0:
23                lt = lt[:idx-1] + lt[idx+1:]
24            else:
25                lt = lt[idx+1:]
26        #print(lt)
27
28        return ls==lt