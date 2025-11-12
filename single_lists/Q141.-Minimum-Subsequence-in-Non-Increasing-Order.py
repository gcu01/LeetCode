class Solution(object):
    def minSubsequence(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # optimization 1
        nums.sort(reverse=True)
        snums = sum(nums)
        #print("snums=", snums)
        my_sum = 0
        for i in range(len(nums)):
            my_sum += nums[i]
            #print(my_sum)
            if my_sum > (snums-my_sum):
                return nums[0:i+1]
        return []

        # my version
        '''
        out = []
        while len(nums)>0:
            maxim = max(nums)
            nums.remove(maxim)
            out.append(maxim)
            if sum(out)>sum(nums):
                break
        #it is already sorted reverse
        #out.sort(reverse=True)
        return out
        '''