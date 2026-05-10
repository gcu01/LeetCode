1class Solution(object):
2    def twoSum(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        for i, val in enumerate(nums):
9            if target-val in nums[i+1:]:
10                j = i+1 + nums[i+1:].index(target-val)
11                return[i, j]
12        