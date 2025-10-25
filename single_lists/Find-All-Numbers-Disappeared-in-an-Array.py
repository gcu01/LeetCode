class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        #optimized 2
        out = []
        s = set(nums)
        for i in range(1, len(nums)+1):
            if i not in s:
                out.append(i)
        return out
        #optimized 1 - very pythonian
    '''    
        n = len(nums)
        perfect = list(range(1, n + 1))
        return list(set(perfect) - set(nums))
    '''
        #my version -not working
    '''
        out = []
        n = len(nums)
        #nums.sort()
        to_work = list(set(nums))#.sort()
        print(to_work)
        to_add = n - len(to_work)
        i = 1
        print(to_add)
        while i < len(to_work) and to_add>=0:
            print(to_work[i])
            print(to_work[i-1])
            print("---")
            if to_work[i] != (to_work[i-1]+1):
                j = 0
                while j<(to_work[i]-to_work[i-1]-1):
                    out.append(to_work[i-1]+j+1)
                    j +=1
                to_add -= 1
            i += 1
        return out
    '''