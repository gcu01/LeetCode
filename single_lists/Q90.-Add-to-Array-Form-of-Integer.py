class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """

        #optimization
        reminder = k
        i = len(num)-1
        
        while i>=0 and reminder>0:
            num[i] += reminder
            #print(num[i])
            if num[i]>=10:
                reminder = num[i]//10
                num[i] %= 10
            else:
                reminder = 0
            i -= 1
        #print(reminder) 
        while reminder>0:
            num.insert(0, reminder%10)
            reminder //= 10
        return num

        # my version 
        '''
        kl = []
        while (k//10)>0:
            kl.append(k%10)
            k //= 10
            #n -= 1       
        kl.append(k)             
        kl.reverse()
        #print("after reverse kl = ", kl)
        diff = len(kl) - len(num)
        if diff > 0:
            while diff > 0:
                num.insert(0,0)
                diff -= 1
        elif diff < 0:
            while diff<0:
                kl.insert(0,0)
                diff += 1
        #print("kl = ", kl)
        #print("num = ", num)
        reminder = 0
        for i in range(len(num)-1, -1, -1):
            num[i] += kl[i] + reminder
            #print("num[i]=", num[i], " where i = ", i)
            if num[i] >= 10:
                reminder = num[i]//10
                #print("inside reminder=", reminder)
                num[i] %= 10
                #print("inside num[i]=", num[i])
            else:
                reminder = 0
        #print(num)
        if reminder > 0:
            num.insert(0,reminder)
        return num
        '''