class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """

        counter = 0.05*len(arr)
        #print(counter)
        while counter!=0:
            arr.remove(max(arr))
            arr.remove(min(arr))
            counter -= 1
        #print(arr)
        #print(sum(arr))
        #print(len(arr))
        return float(sum(arr))/len(arr) if len(arr) else 0