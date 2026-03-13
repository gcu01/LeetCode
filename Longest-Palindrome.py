1class Solution(object):
2    def longestPalindrome(self, s):
3        """
4        :type s: str
5        :rtype: int
6        """
7        d = {}
8        r = 0
9        for c in s:
10            d[c] = d.get(c, 0) + 1
11        for v in d.values():
12            r += v if v % 2 == 0 else v - 1
13        return r + 1 if r < len(s) else r
14
15
16        if len(s) < 2:
17            return len(s)
18        s_dict = dict()
19        for val in s:
20            s_dict[val] = s_dict.get(val, 0) + 1
21            '''
22            if val in s_dict.keys():
23                s_dict[val] += 1
24            else:
25                s_dict[val] = 1
26            '''
27        print(s_dict.values())
28        out = 0
29        pal_lst = sorted(s_dict.items(), key=lambda item: item[1], reverse=True)
30        print("pal_lst = ", pal_lst )
31        for v in s_dict.values():
32            out += v if v % 2 == 0 else v - 1
33        '''
34        for i in range(len(pal_lst)):
35            if pal_lst[i][1] %2 != 0:
36                out += pal_lst[i][1]
37                break
38
39        for i in range(len(pal_lst)):
40            if pal_lst[i][1] %2 == 0:
41                out += pal_lst[i][1]
42        '''
43        return out