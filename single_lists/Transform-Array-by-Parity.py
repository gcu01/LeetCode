1class Solution(object):
2    def transformArray(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        out = []
8        for val in nums:
9            if val%2 == 0:
10                out.insert(0,0)
11            else:
12                out.append(1)
13        return out