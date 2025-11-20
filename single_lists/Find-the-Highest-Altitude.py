class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        maxim = 0
        altitude = 0
        for val in gain:
            altitude += val
            if maxim < altitude:
                maxim = altitude
        return maxim