class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        if len(arr)<3:
            return False
        increase = 0
        decrease = 0
        for i in range(1,len(arr)):
            if arr[i-1]<arr[i]:
                if decrease>0:
                    return False
                increase += 1
            elif arr[i-1]==arr[i]:
                return False
            else:
                if increase<1:
                    return False
                decrease += 1
        if decrease<1:
            return False
        return True
        