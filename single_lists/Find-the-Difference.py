1class Solution(object):
2    def findTheDifference(self, s, t):
3        """
4        :type s: str
5        :type t: str
6        :rtype: str
7        """
8        #ls = list(s)
9        sum_s = sum(ord(x) for x in s)
10        #lt = list(t)
11        sum_t = sum(ord(x) for x in t)
12        x = sum_t - sum_s
13        return chr(x)
14        #out = [x for x in lt if x not in ls]
15        #return out[0] if len(out) else ""
16        
17        '''
18        for val in t:
19            if val in s:
20                s = s.replace(val, "")
21            else:
22                print(s)
23                return val
24
25        return ""
26        '''