1class Solution(object):
2    def maxSubsequence(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: List[int]
7        """
8        d = dict()
9        for i, val in enumerate(nums):
10            d[i] = val
11        #print(d.items())
12        lst = sorted(d.items(), key= lambda x:x[1], reverse = True)
13        #print ("lst1=", lst)
14        lst = sorted(lst[:k], key= lambda x:x[0])
15        #print("lst2=", lst)
16        out = []
17        for key, val in lst:
18            out.append(val)
19        return out
20        
21        
22        
23        out = []
24        i = 0
25        idx = []
26        while i < k:
27            mx = max(x for x in nums if x not in out)
28            out.append(mx)
29            idx.append(nums.index(mx))            
30            #print("mx=", mx, "  out= ", out, "   idx=", idx)
31            i += 1
32        print("idx=", idx)
33        out = []
34        while len(idx):
35            mn = min(idx)
36            out.append(nums[mn])
37            idx.remove(mn)
38        return out
39        
40