class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = 0
        for val in nums:
            if len(str(abs(val)))%2 == 0:
                out += 1
        return out
        