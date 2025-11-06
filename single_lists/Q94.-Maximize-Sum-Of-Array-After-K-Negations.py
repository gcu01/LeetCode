class Solution(object):
    def largestSumAfterKNegations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        print(nums)
        while k>0:
            nums[0] = -nums[0]
            nums.sort()
            k -= 1
        #print(nums)
        return sum(nums)
