1class Solution(object):
2    def reverseWords(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        #lst = s.split(" ")[::-1]
8        #print("lst=", lst)
9        #return " ".join(lst)
10        return " ".join(s.split()[::-1])
11
12
13        # too much time
14        out = []
15        start, end = 0,0
16        #print("size=", len(s))
17        while start < len(s) and end < len(s):
18            if s[start] == " ":
19                start += 1 
20                end = start
21            elif s[end]!= " ":
22                end += 1
23                #print("end=", end)          
24            else:
25                out.append(s[start:end])
26                #print("out=", out)
27                start = end
28                #print("gata s[start] = ", s[start])
29                
30        #print("s[start]=", s[start])
31        #print("s[end]=", s[end])
32        if start < len(s) and s[start] != " ":
33            out.append(s[start:])
34        #print(out)
35        out.reverse()
36        return " ".join(out) 