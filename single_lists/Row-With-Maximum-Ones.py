1class Solution(object):
2    def rowAndMaximumOnes(self, mat):
3        """
4        :type mat: List[List[int]]
5        :rtype: List[int]
6        """
7        # improved version
8        out = [0,0]
9        s = -1
10        for i, val in enumerate(mat):
11            s = sum(val)
12            if s > out[-1]:                
13                out = [i, s]                
14        return out
15
16        # my version
17        '''
18        max_one = -999999
19        idx = 9999999
20        for i, val in enumerate(mat):
21            if 1 in val:
22                if max_one < val.count(1):
23                    max_one = val.count(1)
24                    idx = i
25                elif max_one == val.count(1) and idx > i:
26                    idx = i
27        return [idx, max_one] if idx != 9999999 and max_one != -999999 else [0,0]
28        '''