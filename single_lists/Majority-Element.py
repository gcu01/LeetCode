class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    #optimized solution
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate==num else -1)
        return candidate
    #my solution using a dictionary
    '''
        recurence = {}
        while len(nums)>0:
            elem = nums[len(nums)-1]
            duplication=0
            for j in range(len(nums)-2, -1, -1):
                if elem == nums[j]: 
                    duplication += 1
                    del nums[j]
            recurence[elem] = duplication
            del nums[len(nums)-1]

        recurence = sorted(recurence.items(), key=lambda item: item[1], reverse=True)
        key, value = recurence[0]
        return key
    '''        