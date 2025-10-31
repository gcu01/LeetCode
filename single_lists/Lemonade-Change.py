class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # MY VERSION 2- improved 
        five = 0
        ten = 0
        
        for i in range(len(bills)):
            if bills[i] == 5:
                five +=1
            elif bills[i] == 10:
                ten += 1
                if five >= 1:
                    five -= 1
                else:
                    return False
            else:                
                if ten>=1 and five>=1:
                    ten -= 1
                    five -= 1
                elif five>=3:
                    five -= 3
                else:
                    return False
        return True



        # my version 1 
    '''
        five = []
        ten = []
        twenty = []
        for i in range(len(bills)):
            if bills[i] == 5:
                five.append(5)
            elif bills[i] == 10:
                ten.append(10)
                if len(five) >= 1:
                    five.pop()
                else:
                    return False
            else:
                twenty.append(20)
                if len(ten)>=1 and len(five)>=1:
                    ten.pop()
                    five.pop()
                elif len(five)>=3:
                    five.pop()
                    five.pop()
                    five.pop()
                else:
                    return False
        return True
    '''