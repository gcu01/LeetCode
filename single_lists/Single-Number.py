class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

    #optimized
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]
        return result

    #my version
'''    
        duplicate_found = 0
        repeat = len(nums)/2
        while  repeat >= 0:
            elem = nums[len(nums)-1]
            for i in range(len(nums)-2, -1, -1):
                duplicate_found = 0
                if elem == nums[i]:
                    print("to del=", nums[len(nums)-1])
                    del nums[len(nums)-1]
                    del nums[i]
                    duplicate_found = 1
                    break
            if duplicate_found == 0: return elem
            repeat -= 1
        print (nums)
        return nums[0]
'''