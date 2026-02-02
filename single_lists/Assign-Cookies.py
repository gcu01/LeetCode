1class Solution(object):
2    def findContentChildren(self, g, s):
3        """
4        :type g: List[int]
5        :type s: List[int]
6        :rtype: int
7        """
8        g.sort()
9        s.sort()
10        out = 0
11
12        i, j = 0, 0
13        while i < len(s) and j < len(g):
14            if s[i] >= g[j]:
15                j += 1
16                out += 1
17            i += 1
18        return out
19
20
21        '''
22        while len(g) and len(s):
23            for i in range(len(s)):
24                if s[i] >= g[0]:
25                    g.pop(0)
26                    s.pop(i)
27                    out += 1
28                    break
29                if i == len(s)-1:
30                    return out
31        return out
32        '''
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55        '''
56        res = 0
57        g.sort()
58        s.sort(reverse=True)
59        while len(g) and len(s):
60            #min_g = min(g)
61            #min_s = min(s)
62            print("g = ", g)
63            print("s = ", s)
64            min_g = g[0]
65            min_s = s[0]
66            if min_s >= min_g:
67                res += 1
68            else:
69                break
70            g.pop(0)
71            s.pop(0)
72        return res
73        '''
74        