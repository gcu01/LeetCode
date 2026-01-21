1class Solution(object):
2    def isArraySpecial(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: bool
6        """
7        if len(nums)==1:
8            return True
9        for i in range(1,len(nums)):
10            if nums[i-1]%2 == nums[i]%2:
11                return False
12        return True