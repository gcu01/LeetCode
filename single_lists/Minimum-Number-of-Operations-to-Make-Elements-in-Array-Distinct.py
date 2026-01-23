1class Solution(object):
2    def minimumOperations(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        if len(nums) == len(set(nums)):
8            return 0
9        n = len(nums)
10        i = 0
11        while (3*i+3) < n:
12             
13            if len(nums[3*i+3:]) == len(set(nums[3*i+3:])):
14                i += 1
15                return i
16            i += 1
17        if len(nums[3*i:]) != len(set(nums[3*i:])):
18                i += 1
19        return i