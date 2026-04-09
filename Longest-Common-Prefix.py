1class Solution(object):
2    def longestCommonPrefix(self, strs):
3        """
4        :type strs: List[str]
5        :rtype: str
6        """
7        out = ""
8        
9        if len(strs) < 1:
10            return out
11        elif len(strs[0])<1:
12            return out
13        elif len(strs) < 2:
14            return strs[0]
15        k = 0
16        flag = True
17        while flag:
18            for i in range(1, len(strs)):                
19                if len(strs[i]) < 1 or  k+1 > len(strs[0]) or k+1 > len(strs[i]) or strs[0][k] != strs[i][k]:
20                    flag = False
21            if flag == True:                
22                out += strs[0][k]
23                k += 1
24            
25        return out