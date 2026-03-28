1class Solution(object):
2    def average(self, salary):
3        """
4        :type salary: List[int]
5        :rtype: float
6        """
7        minn = min(salary)
8        maxx = max(salary)
9        return (sum(salary)-minn-maxx)*1.0/(len(salary)-2)