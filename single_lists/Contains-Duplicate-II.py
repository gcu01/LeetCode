class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
    #optimization 1 - create a dict
        duplication = {}
        for idx, val in enumerate(nums):
            if val in duplication:
                if abs(idx-duplication[val])<=k:
                    #print(val,idx)
                    return True
            #else:
            duplication[val]=idx
            #print(duplication)
        return False

    
    # brute-force takes too much time
'''
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j] and abs(i-j)<=k:
                    #print("i=",i,"  j=",j)
                    #print("nums[i]=",nums[i],"  nums[j]=", nums[j])
                    return True
        return False
'''