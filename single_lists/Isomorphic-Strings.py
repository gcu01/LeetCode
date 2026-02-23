1class Solution(object):
2    def isIsomorphic(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: bool
7        """
8        d = dict()
9        out = []
10        for i, val in enumerate(s):
11            #print(d.items())
12            if val in d.keys():
13                if d[val] != t[i]:
14                    #print("false = ", d[val], "  t=", t[i])
15                    return False
16            else:
17                d[val] = t[i]
18                if t[i] in out:
19                    return False
20                else:
21                    out.append(t[i])
22        return True
23        