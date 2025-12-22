1class Solution(object):
2    def findKthPositive(self, arr, k):
3        """
4        :type arr: List[int]
5        :type k: int
6        :rtype: int
7        """
8        maxim = max(arr)
9        l = list(range(1, maxim+k+1))
10        #print("l = ", l)
11        i = 0
12        while k:
13            if l[i] not in arr:
14                #print("l[i] not in l", l[i])
15                if k == 1:
16                    return l[i]
17                k -= 1
18            i += 1
19        return ""
20        
21
22        '''
23        maxim = max(arr)
24        asc = list(range(1, maxim))
25        '''
26        '''
27        j = 0
28        for i in range(len(asc)):
29            if asc[i] != arr[j]:
30                k -= 1
31            else:
32                j += 1
33            if k == 0:
34                return  
35        '''