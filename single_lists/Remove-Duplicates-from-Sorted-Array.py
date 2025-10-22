class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums=="":
            return 0

        res = 1
        i = 1
        while i < len(nums):
            #print(i)
            if nums[i-1] != nums[i]:
                nums[res] = nums[i]
                res = res+1              
            i = i+1
        #print(nums)
        return res
        