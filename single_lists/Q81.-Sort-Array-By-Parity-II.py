class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort(key=lambda x: x % 2) 
        for i in range(len(nums)//2):
            if i%2==0 and nums[i]%2!=0:
                nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
            elif i%2!=0 and nums[i]%2==0:
                nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
        return nums
