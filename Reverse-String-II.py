1class Solution(object):
2    def reverseStr(self, s, k):
3        """
4        :type s: str
5        :type k: int
6        :rtype: str
7        """
8        if len(s)<k:
9            return s[::-1]
10        elif len(s)<2*k:
11            #print("s=", s[0:k][::-1])
12            s=s[0:k][::-1]+s[k:]
13            return s
14        out = ""
15        i = 0
16        while i < len(s):
17            out += s[i:i+k][::-1]
18            i += k
19            if (i+k)<len(s):
20                out += s[i:i+k]
21            else:
22                out += s[i:]
23                break
24            i += k
25            
26        return out
27