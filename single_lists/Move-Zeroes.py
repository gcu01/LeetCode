class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
    #optimized 1
        last_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_zero] = nums[i]
                last_zero += 1
        for i in range(last_zero, len(nums)):
            nums[i] = 0

    #my version 2 -this is not in-place, directly on nums
'''
        singles = set(nums)
        diff = (len(nums) - len(singles)) if next(iter(singles))!=0 else (len(nums) - (len(singles) -1))
        if next(iter(singles))==0:
            singles.remove(min(singles))

        nums[:] = list(singles)
        print(nums)
        while diff:
            nums.append(0)
            diff -= 1

        #print(nums)
'''
    #my version 1
'''
        for i in range(len(nums)-1, -1, -1):
            if nums[i]==0:
                del nums[i]
                nums.append(0)
        print(nums)
        return nums
'''