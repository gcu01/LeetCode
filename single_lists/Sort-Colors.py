1class Solution(object):
2    def sortColors(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: None Do not return anything, modify nums in-place instead.
6        """
7
8        low, mid, hi = 0, 0 , len(nums)-1
9
10        while mid <= hi:
11            if nums[mid] == 0:
12                nums[low], nums[mid] = nums[mid], nums[low]
13                low += 1
14                mid += 1         
15            elif nums[mid] == 2:
16                nums[hi], nums[mid] = nums[mid], nums[hi]
17                hi -= 1
18            else:
19                mid += 1
20            
21
22
23
24
25        '''
26        zero = nums.count(0)
27        one = nums.count(1)
28        two = nums.count(2)
29        z = [0] * zero
30        o = [1] * one
31        t = [2] * two
32        nums = z + o + t
33        print(nums)
34        '''
35
36
37
38        '''
39        n = len(nums)
40        left, right = 0, n-1
41        while left < n and right>=0:
42            print("left = ", left, "   right = ", right)
43            if nums[left] == 2:
44                print("LEFT   bef nums = ", nums, "   left=", left, "   right=", right)
45                del nums[left]
46                #nums.insert(-1, 2)
47                nums.append(2)
48                right -= 1
49                print("LEFT   after nums = ", nums, "   left=", left, "   right=", right)                
50            else:
51                left += 1
52
53            if nums[right] == 0:
54                print("RIGHT   bef nums = ", nums, "   left=", left, "   right=", right)
55                del nums[right]
56                nums.insert(0, 0)
57                left += 1
58                print("RIGHT   bef nums = ", nums, "   left=", left, "   right=", right)
59            else:
60                right -= 1
61        
62        print("left=", left, "   right=", right)
63        
64        if left == right:
65            if nums[left] == 2:
66                del nums[left]
67                nums.append(2)
68            elif nums[left] == 0:
69                del nums[left]
70                nums.insert(0, 0)
71  
72        '''