1class Solution(object):
2    def twoSum(self, numbers, target):
3        """
4        :type numbers: List[int]
5        :type target: int
6        :rtype: List[int]
7        """
8        # improved
9
10        start, end = 0, len(numbers)-1
11
12        while start < end:
13            total = numbers[start] + numbers[end]
14            if total < target:
15                start += 1
16            elif total > target:
17                end -= 1
18            else:
19                return [start+1, end+1]
20        return []
21
22        # takes too much time
23        n = len(numbers)
24        for i in range(n):
25            if (target-numbers[i]) in numbers[i+1:]:
26                #print("2nd idx=", numbers.index(target-numbers[i], i+1, n)+1)
27                return [i+1, numbers.index(target-numbers[i], i+1, n)+1]
28        return []