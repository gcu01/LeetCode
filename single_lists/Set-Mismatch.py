class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        d = 0
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i-1] == nums[i]:
                d = nums[i]
                break  
        
        n_set = list(set(nums))
        for val in range(1,len(nums)+1):
            if val not in n_set:
                return [d,val]
        return []

