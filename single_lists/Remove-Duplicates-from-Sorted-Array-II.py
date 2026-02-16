1class Solution(object):
2    def removeDuplicates(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        if len(nums)<3:
8            return len(nums)
9        k = len(nums)
10        #for i in range(2, len(nums)):
11        i = 2
12        while (k-2) > 0:
13            #print("nums = ", nums)
14            #print(" i = ", i , "nums[:i]=", nums[:i], "   count = ", nums[:i].count(nums[i]))
15            if nums[:i].count(nums[i]) >= 2:
16                #print("before nums = ", nums)
17                nums.pop(i)
18                #print("after nums = ", nums)
19            else:
20                i += 1  
21            k -= 1  
22        return len(nums)
23                
24
25        '''
26        out = []
27        for val in nums:
28            print("val=", val, "  count=", out.count(val))
29            if out.count(val) < 2:
30                out.append(val)
31            print("out=", out)
32            print("-------------")
33        return len(out)
34        '''
35
36
37
38
39        '''
40        input = [4,6,2,4,9,67,5,432,4,56,12,146,99,78,87]
41        #print("before in=", input)
42        n = len(input)
43        for i in range(0, n):
44            min_i = i
45            for j in range(i+1, n):
46                if input[min_i] > input[j]:                                      
47                    min_i = j
48
49            input[i], input[min_i] = input[min_i], input[i]
50        #print("after in=", input)
51
52        class Stack :
53            def __init__(self):
54                self.stack = []
55            def pop(self):
56                if self.stack == []:
57                    print("empty stack")
58                    return ""
59                else:
60                    return self.stack.pop()
61            def append(self, val):
62                return self.stack.append(val)
63            def isEmpty(self):
64                return True if self.stack==[] else False
65            def peek(self):
66                if self.stack == []:
67                    print("Stack is empty")
68                else:
69                    return self.stack[-1]
70            def size(self):
71                return len(self.stack)
72            def printme(self):
73                print("stack = ", self.stack)
74                return ""
75
76        s = Stack()
77        s.append(5)
78        s.append(6)
79        s.printme()
80        p = s.peek()
81        print("peek=",p)
82        s.pop()
83        s.printme()
84        '''