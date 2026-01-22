1class Solution(object):
2    def getSneakyNumbers(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        out = []
8        for val in nums:
9            if nums.count(val) > 1 and val not in out:
10                out.append(val)
11        return out
12