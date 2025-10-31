class Solution(object):
    def isMonotonic(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # my version
        increase = False
        decrease = False
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if increase == 1:
                    return False
                decrease = 1
                increase = 0
            elif nums[i-1]==nums[i]:
                pass
            else:
                if decrease == 1:
                    return False
                increase = 1
                decrease = 0
        return True