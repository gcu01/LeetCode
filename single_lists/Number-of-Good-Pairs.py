class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = 0

        while nums:
            #print("-----------------")
            #print("nums=",nums)
            #print("nums[0]=",nums[0])
            #print("out = ", out)
            for i in range(len(nums)-1, 0, -1):
                #print("nums[",i,"]=",nums[i])
                if nums[0] == nums[i]:
                    out += 1
            del nums[0]
        return out
