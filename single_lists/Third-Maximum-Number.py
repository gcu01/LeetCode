class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #my version
        out = list(set(nums))
        out.sort()
        if len(out)>=3:
            return out[len(out)-3]
        return out[len(out)-1]
        