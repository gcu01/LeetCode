1class Solution(object):
2    def subarraySum(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        s = 0
8        for i in range(len(nums)):
9            m = max(0, i-nums[i])
10            s += sum(nums[m:i+1])
11        return s