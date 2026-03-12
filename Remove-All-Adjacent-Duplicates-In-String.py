1class Solution(object):
2    def removeDuplicates(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7        # optimized
8        i = 0
9        while i < len(s)-1:
10            if s[i] == s[i+1]:
11                s = s[:i] + s[i+2:]
12                i = i-1 if i !=0 else 0
13            else:
14                i += 1
15        return s
16        # takes too much time
17        '''
18        while len(s)>1:
19            for i in range(1, len(s)):
20                if s[i-1] == s[i]:
21                    ls = list(s)
22                    #print("ls=", ls)
23                    ls.pop(i-1)
24                    ls.pop(i-1)
25                    #print("new ls=", ls)
26                    s = "".join(ls)
27                    #print("new s = ", s)
28                    break
29                if i == len(s)-1:
30                    return s
31        return s
32        '''