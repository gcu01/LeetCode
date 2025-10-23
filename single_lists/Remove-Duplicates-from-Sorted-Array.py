class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums=="":
            return 0

        res = 1        
        for i in range(1, len(nums)):
            #print(i)
            if nums[i-1] != nums[i]:
                nums[res] = nums[i]
                res += 1              
        #print(nums)
        return res
        