1class Solution(object):
2    def averageValue(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        sum = 0
8        n = 0
9        for val in nums:
10            if val %6 == 0:
11                sum += val
12                n += 1
13        return 0 if sum==0 else sum/n