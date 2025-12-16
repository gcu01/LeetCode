1class Solution(object):
2    def minNumber(self, nums1, nums2):
3        """
4        :type nums1: List[int]
5        :type nums2: List[int]
6        :rtype: int
7        """
8        minim = 999999
9        for val in nums1:
10            if val in nums2 and minim >val:
11                minim = val
12        if minim != 999999:
13            return minim
14        m1 = min(nums1)
15        m2 = min(nums2)
16        if m1>m2:
17            lm = len(str(abs(m1)))
18            #print("m1=", m1, "  m2=", m2, "  lm=", lm)
19            return m2*(10**lm) + m1
20        else:
21            lm = len(str(abs(m2)))
22            #print("m1=", m1, "  m2=", m2, "  lm=", lm)
23            return m1*(10**lm) + m2
24        
25        return ""