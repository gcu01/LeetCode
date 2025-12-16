1class Solution(object):
2    def countSeniors(self, details):
3        """
4        :type details: List[str]
5        :rtype: int
6        """
7        sixty = 0
8        for val in details:
9            if int(val[11:13])>60:
10                sixty += 1
11        return sixty
12