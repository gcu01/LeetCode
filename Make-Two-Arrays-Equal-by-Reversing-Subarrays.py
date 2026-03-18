1class Solution(object):
2    def canBeEqual(self, target, arr):
3        """
4        :type target: List[int]
5        :type arr: List[int]
6        :rtype: bool
7        """
8        if len(target) != len(arr) or sorted(arr) != sorted(target):
9            return False
10        return True