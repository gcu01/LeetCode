1class Solution(object):
2    def isTrionic(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: bool
6        """
7        if len(nums) < 4:
8            return False
9        p, q = 0, 0
10
11        for i in range(1, len(nums)):     
12            print("nums[i]=", nums[i])       
13            if nums[i] > nums[i-1]:                                
14                if q > 0:
15                    incr = sorted(set(nums[i-1:]))
16                    if incr == nums[i-1:]:
17                        #print("creste -> True  for nums[i]=", nums[i])
18                        return True                                                
19                    return False
20                p += 1
21                #print("creste p = ", p, "   for nums[i]=", nums[i])
22            elif nums[i] < nums[i-1]:
23                if p == 0:
24                    return False            
25                if p > 0 :
26                    q+=1
27                    #print("scade q =", q, "   for nums[i]=", nums[i])
28            elif nums[i] == nums[i-1]:
29                #print("equals -> False")
30                return False
31        
32        return False
33            
34        