class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # optimization 1
        for val in nums:
            if nums.count(val)>1:
                return val

        # my version - better for a list where its values are repeteating more than once. 
        # in our case, only one value repeat itself
        '''
        nums.sort()
        #print(nums)
        count = {}
        for val in nums:
            if val in count:
                count[val] += 1
            else:
                count[val] = 1
        #print(count)
        max = 0
        key_out = -1
        for key,val in count.items():
            #print(key, val)
            if val > max:
                max = val
                key_out = key 
        return key_out
        #out = dict(sorted(count.items(), key=lambda x: x[1], reverse=False))
        #print(out)
        #print( next(iter(out.values())))
        '''