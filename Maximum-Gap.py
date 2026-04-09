1class Solution(object):
2    def maximumGap(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        if len(nums)<2:
8            return 0
9        nums.sort()
10        max = 0
11        for i in range(1, len(nums)):
12            if nums[i]-nums[i-1] > max:
13                max = nums[i] - nums[i-1]
14        return max