1class Solution(object):
2    def findNonMinOrMax(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        if len(nums)<=2:
8            return -1
9        nums.remove(min(nums))
10        nums.remove(max(nums))
11        return nums[0]