1class Solution(object):
2    def evenNumberBitwiseORs(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7
8        res = 0
9        for val in nums:
10            if val % 2 == 0:
11                res |= val
12                
13        return res 