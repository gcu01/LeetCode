1class Solution(object):
2    def numberOfPairs(self, nums1, nums2, k):
3        """
4        :type nums1: List[int]
5        :type nums2: List[int]
6        :type k: int
7        :rtype: int
8        """
9        out = 0
10        for i in range(len(nums1)):
11            for j in range(len(nums2)):
12                if nums1[i] % (nums2[j]*k) == 0:
13                    out += 1
14        return out