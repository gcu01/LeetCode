1class Solution(object):
2    def getFinalState(self, nums, k, multiplier):
3        """
4        :type nums: List[int]
5        :type k: int
6        :type multiplier: int
7        :rtype: List[int]
8        """
9        i = 0
10        while i<k:
11            m = min(nums)
12            idx = nums.index(m)
13            nums[idx] *= multiplier
14            i += 1
15        return nums