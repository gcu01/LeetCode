class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        for val in arr:   
            if (val == 0 and arr.count(0)>=2) or (val!=0 and val%2==0 and (val/2) in arr):
                return True
        return False
        