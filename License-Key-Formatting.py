1class Solution(object):
2    def licenseKeyFormatting(self, s, k):
3        """
4        :type s: str
5        :type k: int
6        :rtype: str
7        """
8        s = s.replace("-", "")
9        s = s.upper()
10        #print(s)
11        reminder = len(s) % k
12        #print("reminder=",reminder)
13        out = ""
14        if reminder > 0:
15            out += s[:reminder]
16            if reminder < len(s):
17                out += "-"
18        #print("out=",out)
19        i = reminder
20        while i<len(s):
21            #print("i=", i)
22            out += s[i:i+k]
23            i += k
24            #print("end i=", i)
25            if i < len(s):
26                out += "-"
27
28        return out