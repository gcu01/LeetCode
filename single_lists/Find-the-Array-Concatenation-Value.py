1class Solution(object):
2    def findTheArrayConcVal(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7
8        con = 0
9        while len(nums):
10            if len(nums) == 1:
11                return con + nums[0]
12            #first = nums[0] * (10 ** len(str(abs(nums[len(nums)-1]))))
13            #print("first = ", first)
14            con += nums[0] * (10 ** len(str(abs(nums[len(nums)-1])))) + nums[len(nums)-1]
15            #print("con = ", con)
16            #print("before remove nums = ", nums)
17            del nums[len(nums)-1]
18            del nums[0]
19            #print("after remove nums = ", nums)           
20        return con
21             
22        