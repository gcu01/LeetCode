class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # optimization 1 - try to walk the list 2 elements at once
        i,j = 0,1
        
        while i<len(nums) and j<len(nums):
            #print(" i = ", i, " J = ", j)
            
            if nums[i]%2 == 0:
                i += 2
            elif nums[j]%2 != 0:
                j += 2
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 2
                j += 2
        return nums

        #my version
        '''
        nums.sort(key=lambda x: x % 2) 
        for i in range(len(nums)//2):
            if i%2==0 and nums[i]%2!=0:
                nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
            elif i%2!=0 and nums[i]%2==0:
                nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
        return nums
        '''