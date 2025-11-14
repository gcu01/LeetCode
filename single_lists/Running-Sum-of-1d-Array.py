class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runSum = 0
        for i in range(len(nums)):
            runSum += nums[i]
            nums[i] = runSum
        return nums