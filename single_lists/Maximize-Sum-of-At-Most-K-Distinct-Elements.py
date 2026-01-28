1class Solution(object):
2    def maxKDistinct(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: List[int]
7        """
8        lst = list(set(nums))
9        lst.sort(reverse=True)
10        return lst[:k]