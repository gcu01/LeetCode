1class Solution(object):
2    def recoverOrder(self, order, friends):
3        """
4        :type order: List[int]
5        :type friends: List[int]
6        :rtype: List[int]
7        """
8        out = []
9        for val in order:
10            if val in friends:
11                out.append(val)
12        #out.reverse()
13        return out