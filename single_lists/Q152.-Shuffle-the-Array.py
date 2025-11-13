class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        idx = 0
        out = []
        while idx < n:
            out.append(nums[idx])
            out.append(nums[idx+n])
            idx += 1
        return out