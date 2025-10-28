class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        #optimized 1
        if n == 0: return True

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1]==0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                #print(flowerbed)
                #print(n)
            if n == 0:
                #print(flowerbed)
                return True
        #print(flowerbed)
        return False
 
        # my version is too complicated
    '''
        if n == 0: return True
        
        for i in range(len(flowerbed)):

            if i == 0 and flowerbed[i] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            elif flowerbed[i] == 1 and (len(flowerbed)-i) >3 and flowerbed[i+1] == flowerbed[i+2]== flowerbed[i+3] == 0 :
                #print("here i=",i, "flowerbed[i]=", flowerbed[i])
                flowerbed[i+2] = 1
                n -= 1
            elif (len(flowerbed)-1) == i and flowerbed[i-1] ==flowerbed[i] == 0:
                n -= 1
            if n == 0:
                return True
        #print(flowerbed)
        return False
    '''