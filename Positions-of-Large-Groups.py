1class Solution(object):
2    def largeGroupPositions(self, s):
3        """
4        :type s: str
5        :rtype: List[List[int]]
6        """
7        idxs, idxe = 0, 0
8        out = []
9        contor = 0
10        for i in range(1,len(s)):
11            #print("i = ", i, "  i-idxs=", i-idxs)
12            if s[i] != s[idxs]:
13                if (i-idxs)>2:
14                    out.append([idxs, i-1])
15                idxs=i
16            elif i == (len(s)-1) and (i-idxs)>1:
17                out.append([idxs, i])
18        #print(out)
19        return out