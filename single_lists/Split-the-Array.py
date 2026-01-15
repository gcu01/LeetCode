1class Solution(object):
2    def isPossibleToSplit(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: bool
6        """
7        n1, n2 = 0, 0
8        nums1, nums2 = [], []
9        n = len(nums)
10        for i in range(len(nums)):
11            if n1 > n-1 or n2 > n-1:
12                return False
13            if nums[i] not in nums1:
14                nums1.append(nums[i])
15                n1 += 1
16            elif nums[i] not in nums2:
17                nums2.append(nums[i])
18                n2 += 1
19            else:
20                return False
21        return True
22        '''
23        for i in range(0, len(nums), 2):
24            if nums[i] not in nums1:
25                nums1.append(nums[i])
26            elif nums[i] not in nums2:
27                nums2.append(nums[i])
28            else:
29                return False
30            if nums[i+1] not in nums1:
31                nums1.append(nums[i+1])
32            elif nums[i+1] not in nums2:
33                nums2.append(nums[i+1])
34            else:
35                return False
36        
37        print("nums1=", nums1)
38        print("nums2=", nums2)
39        if len(nums1) == len(nums2) and len(nums1) == len(nums)/2:
40            return True
41        return False
42        '''