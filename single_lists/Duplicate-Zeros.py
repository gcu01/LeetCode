class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        n = len(arr)-1
        #init_length = 0
        i = 0
        
        while i<=n:
            #print("index = ", i, "  arr[i]=", arr[i])
            #print("arr = ", arr)
            if arr[i] == 0:
                #print("index = ", i, "  arr[i]=", arr[i])
                arr.insert(i+1, 0)
                #init_length += 1
                #print(arr)
                i +=2
                #print("init_length = ", init_length+1, "  i =",i, "   n=", n)
                #print("arr = ", arr)
            else:
                i += 1
            if i >= n:
                del arr[n+1:]
                break
            
        #print(arr)
        