1class Solution(object):
2    def searchInsert(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8
9        start = 0
10        end = len(nums)-1
11        mid = 0
12
13        while start <= end:
14            mid = start + (end - start) / 2
15            if target == nums[mid]:
16                return mid
17            elif target < nums[mid]:
18                end = mid - 1
19            else:
20                start = mid + 1 
21
22        return mid + 1 if target > nums[mid] else mid
23
24
25