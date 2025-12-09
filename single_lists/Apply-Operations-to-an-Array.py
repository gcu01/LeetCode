1class Solution(object):
2    def applyOperations(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: List[int]
6        """
7        for i in range(len(nums)-1):
8            if nums[i] == nums[i+1]:
9                nums[i] *= 2
10                nums[i+1] = 0
11        #print("nums = ", nums)
12        #  too expensive
13        '''
14        for i in range(len(nums)-1):
15            if nums[i] == 0:
16                for j in range(i+1, len(nums)):
17                    if nums[j] !=0 :
18                        nums[i], nums[j] = nums[j], nums[i]
19                        break
20        '''
21        j = 0
22        for i in range(len(nums)):
23            if nums[i] != 0:
24                nums[j], nums[i] = nums[i], nums[j]
25                j += 1
26        return nums