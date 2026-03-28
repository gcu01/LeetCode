1class Solution(object):
2    def frequencySort(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        freq = Counter(nums)
8        nums.sort(key = lambda x:(freq[x], -x))
9        return nums
10
11
12        d = dict()
13        for val in set(nums):
14            d[val] = nums.count(val)
15        print(d)
16        sd = (sorted(d.items(), key=lambda x: x[1]))
17        print(sd)
18        out = []
19        for key, value in sd:
20            i = 0
21            while i<value:
22                out.append(key)
23                i += 1
24        return out
25        