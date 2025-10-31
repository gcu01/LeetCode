class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
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