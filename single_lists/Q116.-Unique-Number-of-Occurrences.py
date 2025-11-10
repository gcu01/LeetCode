class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        # optimization 1
        c = Counter(arr)
        return len(c.values()) == len(list(set(c.values())))


        # my version
        '''
        occurrences = []
        i = 0
        while len(arr)>0:
            #print("arr[0]= ", arr[0])
            duplication = arr.count(arr[0])
            #print("duplication = ", duplication)
            occurrences.append(duplication)
            arr = [x for x in arr if x != arr[0]]
            #print(arr)
        #print(occurrences)
        return len(occurrences) == len(list(set(occurrences)))
        '''