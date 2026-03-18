1class Solution(object):
2    def arrayRankTransform(self, arr):
3        """
4        :type arr: List[int]
5        :rtype: List[int]
6        """
7        # optimized
8
9
10        # takes too much time
11        arr_sort = sorted(set(arr))
12        arr_d = dict()
13        for i, val in enumerate(arr_sort):
14            arr_d[val] = arr_d.get(val, 0) + i +1
15        #print(arr_sort)
16        out = [0]*len(arr)
17        for i, val in enumerate(arr):
18            out[i] = arr_d[val]
19        return out