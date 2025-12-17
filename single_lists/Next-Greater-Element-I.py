1class Solution(object):
2    def nextGreaterElement(self, nums1, nums2):
3        """
4        :type nums1: List[int]
5        :type nums2: List[int]
6        :rtype: List[int]
7        """
8        out = []
9        for val1 in nums1:
10            idx = nums2.index(val1)
11            found = False
12            for val2 in nums2[idx+1:]:
13                if val2>val1:
14                    out.append(val2)
15                    found = True
16                    break
17            if found == False:
18                out.append(-1)
19        return out
20            
21
22
23        '''
24        out = []
25        for val1 in nums1:
26            for i, val2 in enumerate(nums2):
27                if val1==val2:
28                    max = -1
29                    for j in range(i+1,len(nums2)):
30                        if nums2[j] > val1:
31                            print(nums2[j])
32                            max = nums2[j] if nums2[j]>max else max
33                    out.append(max)     
34                    break
35        return out
36        '''