1class Solution(object):
2    def distinctAverages(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        s = set()
8        while len(nums):
9            minim = min(nums)
10            maxim = max(nums)
11            #print("minim=",minim, "   maxim = ", maxim)
12            s.add((minim+maxim)/2.0)
13            #print("s=", s)
14            nums.remove(minim)
15            nums.remove(maxim)
16            #print("nums=", nums)
17        #print(s)
18        return len(s)