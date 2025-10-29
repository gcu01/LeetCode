class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #my version 2

        max_nums = 0
        max_list = 0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                max_nums += 1
            else:
                if max_list<max_nums:
                    max_list = max_nums
                max_nums = 0
        if max_list<max_nums:
            max_list = max_nums
        return max_list+1

        # my version 1 - to improve in not using out[]
    '''
        max = 0
        out = []
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                max += 1
            else:
                out.append(max)
                max = 0
        out.append(max)
        out.sort(reverse=True)
        return out[0]+1 if out != [] else 0
    '''