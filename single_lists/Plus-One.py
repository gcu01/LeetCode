class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

#optimized solution when adding 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i] += 1
                return digits
        return [1]+digits

#my solution works bettern when adding a certain value (greater than 1)
'''
        digits.reverse()

        if (digits[0]+1)>=10:
            remainder = (digits[0]+1)//10
            digits[0] = (digits[0]+1)%10 
        else: 
            remainder = 0
            digits[0] = (digits[0]+1)

        i = 0
        for i in range(1,len(digits)):
            if remainder != 0:
                if (digits[i]+remainder)>=10:
                    remainder = (digits[i]+remainder)//10    
                    digits[i] = (digits[i]+remainder)%10
                else:
                    remainder = 0
                    digits[i] = digits[i]+1
            else:
                break
                
        if (i+1) == len(digits) and remainder != 0:
            digits.append(remainder)
        
        digits.reverse()
        return digits
'''