1from itertools import combinations
2
3class Solution(object):
4    def numEquivDominoPairs(self, dominoes):
5        """
6        :type dominoes: List[List[int]]
7        :rtype: int
8        """
9        d = dict()
10        count = 0
11        for elem in dominoes:
12            key = elem[0]*10 + elem[1] if elem[0]>elem[1] else elem[1]*10 + elem[0]
13            count += d.get(key, 0)
14            d[key] = d.get(key, 0) + 1
15        return count 
16        
17
18        '''
19        d = {}
20        for elem in dominoes:
21            if elem[0]>elem[1]:
22                elem[0], elem[1] = elem[1], elem[0]
23            
24            #d[elem] = d.get(d[elem], 0) + 1
25        dominoes = sorted(dominoes)
26        print(dominoes)
27        '''