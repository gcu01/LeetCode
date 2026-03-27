1class Solution(object):
2    def minimumAbsDifference(self, arr):
3        """
4        :type arr: List[int]
5        :rtype: List[List[int]]
6        """        
7        arr.sort()
8        if len(arr)==2:
9            return [arr]
10        mn = max(arr)
11        for i in range(1, len(arr)):
12            if mn > arr[i]-arr[i-1]:
13                mn = arr[i]-arr[i-1]
14        #print("mn=", mn)
15        
16        out = []
17        for i in range(1, len(arr)):
18            if arr[i-1]+mn == arr[i]:
19                out.append([arr[i-1], arr[i]])
20        '''
21        for i in range(len(arr)):
22            if arr[i]+mn in arr[i+1:]:
23                out.append([arr[i], arr[i]+mn])
24        '''
25        return out