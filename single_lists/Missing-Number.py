class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #optimized version 1
        n = len(nums)
        expected_sum = (n*(n+1))//2
        nums_sum = sum(nums)
        return (expected_sum - nums_sum)

        #my version
    '''    
        nums.sort()
        for i in range(1,len(nums)):
            print("nums[i-1]=", nums[i-1],"  nums[i]=", nums[i])
            if nums[i-1]+1 != nums[i]:
                return nums[i-1]+1
        return (0 if nums[0]!=0 else len(nums))
    '''
