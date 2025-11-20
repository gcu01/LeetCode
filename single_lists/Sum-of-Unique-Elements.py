class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for val in nums:
            if nums.count(val) == 1:
                sum += val
        return sum