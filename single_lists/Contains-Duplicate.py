class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
    #optimization 2 - ordering the list 
        nums.sort()
       #i=0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    #optimization 1 - add each element in a different set(a list -takes too much time), check if exists there
'''
        #duplication = []
        duplication = set()
        for val in nums:
            if val in duplication:
                return True
            #duplication.append(val)
            duplication.add(val)
        return False
'''
    #my version - brute-force - takes too much time
'''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
'''