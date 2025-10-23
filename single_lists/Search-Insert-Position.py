class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        for i, value in enumerate(nums):
            if value == target or value > target:
                return i
        return i+1
            