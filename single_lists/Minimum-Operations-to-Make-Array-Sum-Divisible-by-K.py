1class Solution(object):
2    def minOperations(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        s = sum(nums)
9        if s%k == 0:
10            return 0
11        d = s/k
12        return s-d*k