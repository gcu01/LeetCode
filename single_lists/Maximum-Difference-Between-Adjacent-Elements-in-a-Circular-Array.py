1class Solution(object):
2    def maxAdjacentDistance(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        out = []
8        if len(nums)<2:
9            return 0
10        out.append(abs(nums[len(nums)-1]-nums[0]))
11        for i in range(1, len(nums)):
12            out.append(abs(nums[i]-nums[i-1]))
13        return max(out)