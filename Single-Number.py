1class Solution(object):
2    def singleNumber(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        nums.sort()
8        for i in range(0, len(nums)-1, 2):
9            if nums[i] != nums[i+1]:
10                return nums[i]
11        return nums[-1]