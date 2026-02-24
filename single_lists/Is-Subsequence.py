1class Solution(object):
2    def isSubsequence(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: bool
7        """
8        i, j = 0, 0
9
10        while i < len(s) and j < len(t):
11            if s[i] == t[j]:
12                #print("s[",i,"]=", s[i])
13                i += 1
14            j += 1
15        #print("i=", i)
16        return i == len(s)
17        '''
18        idx = -1
19        for i in range(len(s)):
20            
21            if s[i] in t[idx+1:] : #and t.index(val)>idx :
22                print("val=", s[i], "   idx=", idx)
23                idx = t.index(s[i])
24            else:
25                return False
26            if i < (len(s)-1) and (idx == len(t)-1):
27                return False
28        return True
29
30        '''
31
32
33
34
35
36
37
38        '''
39        lst_s = list(s)
40        lst_t = list(t)
41        idx = len(s)
42        for i, val in lst_t:
43            if val in lst_s
44                lst_idx = [j for j, x in enumerate(lst_s) if x == val]
45                
46            
47             and idx < lst_s.index(val):
48                idx = lst_s.index(val)
49        '''