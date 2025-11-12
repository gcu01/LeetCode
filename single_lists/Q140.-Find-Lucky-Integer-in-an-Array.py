class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        lucky = []
        for val in arr:
            if val == arr.count(val):
                lucky.append(val)
        if lucky == []:
            return -1
        return max(lucky)
        