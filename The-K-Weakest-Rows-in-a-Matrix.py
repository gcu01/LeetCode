1class Solution(object):
2    def kWeakestRows(self, mat, k):
3        """
4        :type mat: List[List[int]]
5        :type k: int
6        :rtype: List[int]
7        """
8        out = []
9        for i, val in enumerate(mat):
10            out.append([sum(val), i])
11        out.sort()
12        #print("out=", out)
13        return [k for j, k in out[:k]]
14
15
16        out = []
17        for i in range(len(mat)):
18            out.append(sum(mat[i]))
19        print("out = ", out)
20        i = 0
21        res = []
22        check = []
23        while i<k:
24            mn = min(x for x in out if x not in check)
25            res.append(out.index(mn))
26            check.append(mn)
27            i += 1
28        return res
29        '''
30        tmp = []
31        for val in out:
32            tmp.append(val)
33        print("tmp=", tmp)
34        out.sort()
35        print("sorted out = ", out)
36        i = 0
37        res = []
38        while i < k:
39            res.append(tmp.index(out[i]))
40            i += 1
41        return res
42        '''