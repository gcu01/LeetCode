1class Solution(object):
2    def isAnagram(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: bool
7        """
8        if len(s) != len(t):
9            return False
10
11        d = dict()
12
13        for ch in s:
14            d[ch] = d.get(ch, 0) + 1
15            '''
16            if ch in d.keys():
17                d[ch] += 1
18            else:
19                d[ch] = 1
20            '''
21        for ch in t:
22            if d.get(ch, 0) == 0 or d[ch] < 1:
23            #if ch not in d.keys() or d[ch] < 1:
24                return False
25            d[ch] -= 1
26        
27        return True
28
29        # takes too much time
30        '''
31        if len(s) != len(t):
32            return False
33
34        out = list(t)
35        for val in s:
36            if val in out:
37                out.remove(val)
38            else:
39                return False
40
41        return True
42        '''