1class Solution(object):
2    def firstUniqChar(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7
8        duplicate = dict()
9
10        for ch in s:
11            duplicate[ch] = duplicate.get(ch, 0) + 1
12        
13        for i, ch in enumerate(s):
14            if duplicate[ch] == 1:
15                return i
16        
17        return -1
18
19
20        '''
21        ls = list(s)
22        duplicates = []
23        for i, val in enumerate(ls):
24            if val not in duplicates and ls[i+1:].count(val) > 0:
25                duplicates.append(val)
26            elif val not in duplicates:
27                #print(duplicates)
28                return i
29        return -1
30        '''
31
32        # takes too much time
33        '''
34        ls = list(s)
35        it_is = []
36        for i, val in enumerate(ls):
37            if val not in ls[i+1:] and val not in it_is:
38                return i
39            it_is.append(val)
40            
41        return -1
42        '''