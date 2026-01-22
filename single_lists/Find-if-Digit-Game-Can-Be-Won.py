1class Solution(object):
2    def canAliceWin(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: bool
6        """
7        single = 0
8        double = 0
9        for val in nums:
10            if val<10:
11                single += val
12            else:
13                double += val
14        return True if single != double else False