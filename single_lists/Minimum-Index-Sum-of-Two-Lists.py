class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        min = -1
        sum = {}
        out = []
        for i, val1 in enumerate(list1):
            for j, val2 in enumerate(list2):
                if val1 == val2:
                    sum[i] = j
        #print(sum)
        
        for key, value in sum.items():
            if min == -1:
                min = key + value
            elif min > (key+value):
                min = key+value
        #print(min)
        for key, value in sum.items():
            if min == key+value:
                out.append(list1[key])
        
        return out