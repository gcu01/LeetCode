1class Solution(object):
2    def removeDuplicates(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """        
7        #if len(nums) < 2:
8        #    return len(nums)
9        k = 0
10        l = len(nums)
11        for i in range(len(nums) - 2, -1, -1):
12            #print("nums[i]=", nums[i], "   nums[i+1]=", nums[i+1])
13            if nums[i] == nums[i + 1]:
14                nums.pop(i+1)
15                k += 1
16                #print("k=",k, "   nums=", nums)        
17        return l-k
18        #return len(nums)-k if k else len(nums) 