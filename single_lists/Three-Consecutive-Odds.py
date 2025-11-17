class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = 0
        for i in range(len(arr)):
            while i<len(arr) and arr[i]%2 == 1:
                count += 1
                i += 1
                if count == 3:
                    return True
            count = 0
        return False
        