class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = max(nums)
        idx = nums.index(maximum)
        nums[idx] = 0
        max_second = max(nums)

        if (maximum//2)>=max_second:
            return idx
        else:
            return -1