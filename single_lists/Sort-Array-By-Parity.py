class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # optimization 3 - working on the same list, rearenging elements, even at the beginning, odd at the end
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i]%2 != 0 and nums[j]%2==0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            elif nums[i]%2 == 0:
                i += 1
            else:
                j -=1
        return nums
        
        # optimization 1 is using another list - better exec time
        '''
        out = []
        for i in range(len(nums)):
            if nums[i] == 0 or nums[i]%2 == 0:
                out.insert(0,nums[i])
            else:
                out.append(nums[i])
        return out
        '''


        # my version is using the same list, better memory usage
        
    '''
        i = len(nums)-1
        j = -1
        while i >= 0:
            #print(j)
            if nums[j] == 0 or nums[j]%2 == 0:
                nums.insert(0,nums[j])
                #j = -1 if j==-1 else 
            else:
                nums.append(nums[j])
                j -= 1
            nums.pop(j)
            i -= 1
        return nums
    '''