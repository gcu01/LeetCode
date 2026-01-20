1class Solution(object):
2    def addedInteger(self, nums1, nums2):
3        """
4        :type nums1: List[int]
5        :type nums2: List[int]
6        :rtype: int
7        """
8        nums1.sort()
9        nums2.sort()
10        x = 0
11        
12        if nums1 == nums2:
13            return x
14        x = nums2[0]-nums1[0]
15        for i in range(len(nums1)):
16            if nums1[i] + x != nums2[i]:
17                return 0
18        return x