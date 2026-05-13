1class Solution(object):
2    def merge(self, nums1, m, nums2, n):
3        """
4        :type nums1: List[int]
5        :type m: int
6        :type nums2: List[int]
7        :type n: int
8        :rtype: None Do not return anything, modify nums1 in-place instead.
9        """
10        if nums1 == []:
11            nums1 = nums2
12        if nums2 == []:
13            return
14        
15        i, j = m-1, n-1
16        k = m + n - 1
17        while i >= 0 and j >= 0:
18            if nums1[i] >= nums2[j]:
19                nums1[k] = nums1[i]
20                i -= 1
21            else:
22                nums1[k] = nums2[j]
23                j -= 1
24            k -= 1
25
26        while j >= 0:
27            nums1[j] = nums2[j]
28            j -= 1