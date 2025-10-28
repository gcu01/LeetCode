class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # optimization 1

        nums.sort(reverse=True)
        # three largest numbers
        option1 = nums[0]*nums[1]*nums[2]
        # one largest number and 2 smalles (maybe they are negatives)
        option2 = nums[0]*nums[len(nums)-1]*nums[len(nums)-2]
        return option1 if option1>option2 else option2

        # my version - it is good but needs to be re-writen for a better exec time
    '''
        prod = 1
        neg_prod = 1
        n = 0
        flag = False
        nums.sort(reverse=True)
        #print(nums)
        if nums[len(nums)-1] <0 and nums[len(nums)-2] <0 and nums[0]>0:
            neg_prod =  nums[len(nums)-1] * nums[len(nums)-2] * nums[0]
            flag = True
        #print(neg_prod)
        #print(flag)
        for i in range(len(nums)):           
            prod *= nums[i]
            n+=1
            if n == 3:
                #print(prod)
                #print(neg_prod)
                if flag == False:
                    return prod
                return prod if prod>=neg_prod else neg_prod
        #print(prod)
        #print(neg_prod)
        return prod
    '''