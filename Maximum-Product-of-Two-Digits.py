1class Solution(object):
2    def maxProduct(self, n):
3        """
4        :type n: int
5        :rtype: int
6        """
7        s = str(n)
8        #print("s=",s)
9        lst = list(s)
10        #print(lst)
11        lst.sort(reverse=True)
12        return int(lst[0])*int(lst[1])