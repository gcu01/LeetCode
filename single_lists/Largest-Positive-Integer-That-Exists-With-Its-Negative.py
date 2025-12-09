1class Solution(object):
2    def findMaxK(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        maxim = -1
8        for val in nums:
9            if maxim < val and -val in nums:
10                maxim = val
11        return maxim