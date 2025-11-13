class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = max(nums)
        idx_i = nums.index(max1)
        #print(idx_i)
        if 0<idx_i and idx_i<len(nums)-1:
            max2 = max(nums[0:idx_i]) if max(nums[0:idx_i]) > max(nums[idx_i+1:]) else max(nums[idx_i+1:])
        elif idx_i == 0:
            max2 =  max(nums[idx_i+1:])
        else:
            max2 =  max(nums[:idx_i])
        #idx_j = nums.index(max2)
        #print(idx_j)
        return (max1-1)*(max2-1)
