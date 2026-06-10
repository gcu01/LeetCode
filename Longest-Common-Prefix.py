1class Solution(object):
2    def longestCommonPrefix(self, strs):
3        """
4        :type strs: List[str]
5        :rtype: str
6        """
7        res = strs[0]
8        for i in range(1, len(strs)):
9            if res == "":
10                return res
11            length = min( len(res), len(strs[i]) )
12            res = res[:length]
13            #print("res = ", res)
14            #print("length = ", length)
15            for idx in range(length):
16                #print("idx = ", idx)
17                if res[idx] != strs[i][idx]:
18                    res = res[:idx]
19                    #print("new res=", res)
20                    break
21        return res
22
23        
24
25
26
27
28
29
30
31
32
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
43        out = ""
44        
45        if len(strs) < 1:
46            return out
47        elif len(strs[0])<1:
48            return out
49        elif len(strs) < 2:
50            return strs[0]
51        k = 0
52        flag = True
53        while flag:
54            for i in range(1, len(strs)):                
55                if len(strs[i]) < 1 or  k+1 > len(strs[0]) or k+1 > len(strs[i]) or strs[0][k] != strs[i][k]:
56                    flag = False
57            if flag == True:                
58                out += strs[0][k]
59                k += 1
60            
61        return out