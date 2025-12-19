1class Solution(object):
2    def replaceElements(self, arr):
3        """
4        :type arr: List[int]
5        :rtype: List[int]
6        """
7        # improved solution 1
8        maxim = arr[-1]
9        for i in range(len(arr)-1, -1, -1):
10            if i == len(arr)-1:
11                arr[i] = -1
12            else:
13                if maxim < arr[i]:
14                    arr[i], maxim = maxim, arr[i]
15                else:
16                    arr[i] = maxim
17        return arr
18
19        # my version takes 2 much time
20        '''
21        for i in range(len(arr)-1):
22            m = max(arr[i+1:])
23            arr[i] = m
24        arr[-1] = -1
25        return arr
26        '''