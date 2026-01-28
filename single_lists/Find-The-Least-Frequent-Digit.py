1class Solution(object):
2    def getLeastFrequentDigit(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        lst = list(str(n))
8        #print(lst)
9        mf, digit = float('inf'), '99999999'
10        
11        for val in lst:
12            if lst.count(val) < mf:
13                #print("mf=", lst.count(val))
14                #print("digit=", digit)
15                #print("------")
16                mf = lst.count(val)
17                digit = val
18            elif lst.count(val) == mf and val < digit:
19                mf = lst.count(val)
20                digit = val
21                
22        return int(digit)