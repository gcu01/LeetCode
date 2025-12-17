1class Solution(object):
2    def semiOrderedPermutation(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        if nums[0] == 1 and nums[-1]==len(nums):
8            return 0
9        idx_one, idx_n = nums.index(1), nums.index(len(nums))
10        
11        return idx_one + len(nums)-idx_n -1 if idx_one < idx_n else idx_one + len(nums)-idx_n -2