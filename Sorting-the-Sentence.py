1class Solution(object):
2    def sortSentence(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        lst = s.split()
8        #print("initial lst = ", lst)
9        #print(lst[0][-1])
10        i = 0
11        while i < len(lst):
12            idx = int(lst[i][-1])
13            #print("idx=", idx)
14            if i+1 != idx:
15                lst[i], lst[idx-1] = lst[idx-1], lst[i]
16            else:
17                i += 1
18        #print("ordered lst = ", lst)
19        out = []
20        for val in lst:
21            ln = len(val)-1
22            out.append(val[:ln])
23        #print("final lst=", out)
24        return " ".join(out)
25
26        '''
27        out = [""]*9
28        for val in lst:
29            idx = val[-1]
30            print("idx=", idx)
31            out[idx] = val
32        return out
33        '''