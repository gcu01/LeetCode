1class Solution(object):
2    def removeOuterParentheses(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        out = ""
8        p = 1
9        idxs = 0
10        for i in range(1, len(s)):
11            if s[i] == "(":
12                p += 1
13                #print("i = ", i, "   p=", p)                
14            else:
15                p -= 1
16                #print("i = ", i, "   p=", p)
17            if p == 0:
18                out += s[idxs+1:i]
19                idxs = i+1 if i<(len(s)-1) else 0
20                #print("out = ", out)
21                #print("idxs = ", idxs)
22        return out
23